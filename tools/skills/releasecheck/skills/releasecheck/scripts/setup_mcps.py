#!/usr/bin/env python3
"""Install and register the MCP servers the releasecheck review steps use.

check_rc.py needs none of these. The review steps in SKILL.md use six, all
read-only, and still work without them at reduced coverage.

What it does:
  1. Clones or updates each server under --dir (default ~/.asf-mcp).
  2. Puts the Python servers in one virtual environment there, and runs
     npm install for the Node one.
  3. Shows what it would add to which config file and asks before changing
     anything. On a yes, backs up each file it will change, then registers
     the servers with Claude Code (user scope) and, when asked, Claude
     Desktop, Codex and OpenCode.

Running it again updates the existing checkouts with git pull rather than
cloning again.

A server already registered under the same name is left alone, so an existing
setup is never overwritten. Standard library only.

    python3 scripts/setup_mcps.py              install and register
    python3 scripts/setup_mcps.py --dry-run    show what would happen
    python3 scripts/setup_mcps.py --desktop    also add to Claude Desktop
    python3 scripts/setup_mcps.py --codex      also add to Codex
    python3 scripts/setup_mcps.py --opencode   also add to OpenCode
    python3 scripts/setup_mcps.py --no-register   install only
    python3 scripts/setup_mcps.py --yes        do not ask before registering
"""

import argparse
import datetime
import json
import os
import shutil
import subprocess
import sys

GITHUB = "https://github.com/justinmclean"

# name: (repo, kind, console script or entry file). The ipmc server pulls in
# its own dependencies (health, reports, mail, releases, podlings, trademark)
# from GitHub when it is installed.
SERVERS = {
    "asf-policy": ("PolicyMCP", "python", "asf-policy-mcp"),
    "incubator-mail": ("MailMCP", "python", "incubator-mail-mcp"),
    "incubator-releases": ("ReleaseMCP", "python", "incubator-releases-mcp"),
    "podlings": ("PodlingsMCP", "python", "podlings-mcp"),
    "ipmc": ("IncubatorMCP", "python", "ipmc-mcp"),
    "apache-projects-mcp": ("apache-projects-mcp", "node", "index.js"),
}

# podlings and ipmc need 3.12; the rest need 3.10 or 3.11.
MIN_PYTHON = (3, 12)

CLAUDE_CODE_CONFIG = os.path.expanduser("~/.claude.json")
if sys.platform == "darwin":
    DESKTOP_CONFIG = os.path.expanduser(
        "~/Library/Application Support/Claude/claude_desktop_config.json")
elif os.name == "nt":
    DESKTOP_CONFIG = os.path.join(os.environ.get("APPDATA", ""), "Claude",
                                  "claude_desktop_config.json")
else:
    DESKTOP_CONFIG = os.path.expanduser("~/.config/Claude/claude_desktop_config.json")

CODEX_CONFIG = os.path.join(os.environ.get("CODEX_HOME") or os.path.expanduser("~/.codex"),
                            "config.toml")
OPENCODE_DIR = os.path.join(os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config"),
                            "opencode")

DRY = False


def say(msg):
    print(msg, flush=True)


def run(cmd, cwd=None):
    say("  $ " + " ".join(cmd))
    if not DRY:
        subprocess.run(cmd, cwd=cwd, check=True)


def find_python(preferred=None):
    # The default python3 first: a newer interpreter found on PATH may have no
    # prebuilt wheels for dependencies such as cryptography.
    for name in ([preferred] if preferred else ["python3", "python3.12", "python3.13", "python"]):
        exe = shutil.which(name)
        if not exe:
            continue
        out = subprocess.run([exe, "-c", "import sys; print(*sys.version_info[:2])"],
                             capture_output=True, text=True)
        if out.returncode == 0 and tuple(map(int, out.stdout.split())) >= MIN_PYTHON:
            return exe
    return None


def fetch(repo, dest):
    if os.path.isdir(os.path.join(dest, ".git")):
        # Already cloned: update it. A checkout with local changes or a
        # diverged branch is kept as it is rather than stopping the run.
        try:
            run(["git", "-C", dest, "pull", "--ff-only", "-q"])
        except subprocess.CalledProcessError:
            say(f"  could not update {dest}; using it as it is")
    else:
        run(["git", "clone", "-q", f"{GITHUB}/{repo}.git", dest])


def venv_bin(venv, name):
    if os.name == "nt":
        return os.path.join(venv, "Scripts", name + ".exe")
    return os.path.join(venv, "bin", name)


def install(root, only, preferred=None):
    need_py = any(SERVERS[n][1] == "python" for n in only)
    need_node = any(SERVERS[n][1] == "node" for n in only)

    python = find_python(preferred) if need_py else None
    if need_py and not python:
        sys.exit(f"need Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or later on PATH")
    for tool in ["git"] + (["node", "npm"] if need_node else []):
        if not shutil.which(tool):
            sys.exit(f"need {tool} on PATH")

    src = os.path.join(root, "src")
    venv = os.path.join(root, "venv")
    commands = {}

    if need_py:
        if not os.path.isdir(venv):
            say(f"creating virtual environment {venv}")
            run([python, "-m", "venv", venv])
        pip = [venv_bin(venv, "python"), "-m", "pip", "install", "-q", "--upgrade"]
        run(pip + ["pip"])

    for name in only:
        repo, kind, entry = SERVERS[name]
        dest = os.path.join(src, repo)
        say(f"\n{name} ({GITHUB}/{repo})")
        fetch(repo, dest)
        if kind == "python":
            run(pip + [dest])
            commands[name] = [venv_bin(venv, entry)]
        else:
            run(["npm", "install", "--omit=dev", "--silent"], cwd=dest)
            commands[name] = [shutil.which("node"), os.path.join(dest, entry)]
    return commands


def backup(path, stamp):
    if not os.path.isfile(path):
        return
    copy = f"{path}.{stamp}.bak"
    say(f"  backup {path} -> {copy}")
    if not DRY:
        shutil.copy2(path, copy)


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return None


def write(path, text):
    if DRY:
        return
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, path)


class Target:
    """One client's config. names() returns the servers already registered,
    or None when the file can't be read safely, in which case it is left
    alone. add() re-reads the file immediately before writing it, so nothing
    changed since the plan was made is lost."""

    label = path = None
    hint = ""

    def names(self):
        raise NotImplementedError

    def add(self, new):
        raise NotImplementedError


class ClaudeCode(Target):
    label, path = "Claude Code", CLAUDE_CODE_CONFIG

    def __init__(self, claude):
        self.claude = claude

    def names(self):
        text = read(self.path)
        try:
            return set(json.loads(text).get("mcpServers", {})) if text else set()
        except ValueError:
            return None

    def add(self, new):
        for name, cmd in new.items():
            run([self.claude, "mcp", "add", "-s", "user", name, "--"] + cmd)


class JsonTarget(Target):
    key = None

    def names(self):
        text = read(self.path)
        try:
            return set(json.loads(text).get(self.key, {})) if text else set()
        except ValueError:
            return None

    def entry(self, cmd):
        raise NotImplementedError

    def add(self, new):
        text = read(self.path)
        config = json.loads(text) if text else self.empty()
        servers = config.setdefault(self.key, {})
        for name, cmd in new.items():
            servers.setdefault(name, self.entry(cmd))
        write(self.path, json.dumps(config, indent=2) + "\n")

    def empty(self):
        return {}


class ClaudeDesktop(JsonTarget):
    label, path, key = "Claude Desktop", DESKTOP_CONFIG, "mcpServers"
    hint = "restart Claude Desktop to pick them up"

    def entry(self, cmd):
        return {"command": cmd[0], "args": cmd[1:]}


class OpenCode(JsonTarget):
    label, key = "OpenCode", "mcp"

    def __init__(self):
        # opencode.jsonc may hold comments, which the json module can't read;
        # names() then returns None and the block is printed to paste instead.
        for name in ("opencode.jsonc", "opencode.json"):
            self.path = os.path.join(OPENCODE_DIR, name)
            if os.path.isfile(self.path):
                break
        else:
            self.path = os.path.join(OPENCODE_DIR, "opencode.json")

    def empty(self):
        return {"$schema": "https://opencode.ai/config.json"}

    def entry(self, cmd):
        return {"type": "local", "command": cmd, "enabled": True}

    def snippet(self, commands):
        body = {n: self.entry(c) for n, c in commands.items()}
        return '"mcp": ' + json.dumps(body, indent=2)


class Codex(Target):
    label, path = "Codex", CODEX_CONFIG

    def names(self):
        text = read(self.path)
        if not text:
            return set()
        try:
            import tomllib
        except ImportError:
            return None
        try:
            return set(tomllib.loads(text).get("mcp_servers", {}))
        except tomllib.TOMLDecodeError:
            return None

    def add(self, new):
        # The standard library reads TOML but can't write it, so new tables
        # are appended as text and everything already there is untouched.
        text = read(self.path) or ""
        have = self.names() or set()
        blocks = [self.block(n, c) for n, c in new.items() if n not in have]
        if text and not text.endswith("\n"):
            text += "\n"
        write(self.path, text + "".join(blocks))

    @staticmethod
    def block(name, cmd):
        # JSON string escapes are valid TOML basic strings.
        args = ", ".join(json.dumps(a) for a in cmd[1:])
        # codex exec never asks for approval, so without this every MCP call is
        # refused. These servers are all read-only.
        return (f"\n[mcp_servers.{name}]\ncommand = {json.dumps(cmd[0])}\nargs = [{args}]\n"
                'default_tools_approval_mode = "approve"\n')

    def snippet(self, commands):
        return "".join(self.block(n, c) for n, c in commands.items())


def targets(args):
    found = []
    claude = shutil.which("claude")
    if args.no_claude_code:
        pass
    elif claude:
        found.append(ClaudeCode(claude))
    else:
        say("\nclaude CLI not found, so Claude Code is skipped")
    wanted = [(args.desktop, ClaudeDesktop, os.path.dirname(DESKTOP_CONFIG)),
              (args.codex, Codex, os.path.dirname(CODEX_CONFIG)),
              (args.opencode, OpenCode, OPENCODE_DIR)]
    for asked, cls, home in wanted:
        if not asked:
            continue
        if os.path.isdir(home):
            found.append(cls())
        else:
            say(f"\n{cls.label} does not look installed ({home} missing), so it is skipped")
    return found


def plan(commands, found):
    """Work out what would be added where, without changing anything."""
    steps = []
    for target in found:
        have = target.names()
        if have is None:
            say(f"\n{target.label}: could not read {target.path}, so it is left alone")
            if hasattr(target, "snippet"):
                say("  add this by hand if you want these servers there:\n")
                say(target.snippet(commands))
            continue
        new = {n: c for n, c in commands.items() if n not in have}
        steps.append((target, new, sorted(set(commands) & have)))
    return steps


def confirm(steps, assume_yes):
    say("\nThis will change your configuration:")
    for target, new, kept in steps:
        say(f"\n  {target.label}: {target.path}")
        for name in new:
            say(f"    add  {name}")
        for name in kept:
            say(f"    keep {name} (already registered, not changed)")
    say("\n  Each file is backed up first, next to the original, as <file>.<timestamp>.bak")
    if assume_yes:
        return True
    if not sys.stdin.isatty():
        say("\nno terminal to confirm on (pass --yes to allow it)")
        return False
    try:
        return input("\nGo ahead? [y/N] ").strip().lower() in ("y", "yes")
    except EOFError:
        return False


def main():
    global DRY
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dir", default=os.path.expanduser("~/.asf-mcp"),
                    help="where servers are cloned and installed (default ~/.asf-mcp)")
    ap.add_argument("--only", nargs="+", choices=sorted(SERVERS), metavar="NAME",
                    help="install only these servers: " + ", ".join(SERVERS))
    ap.add_argument("--python", help="interpreter for the virtual environment (default: first 3.12+ found)")
    ap.add_argument("--desktop", action="store_true", help="also register with Claude Desktop")
    ap.add_argument("--codex", action="store_true", help="also register with Codex (~/.codex/config.toml)")
    ap.add_argument("--opencode", action="store_true", help="also register with OpenCode (~/.config/opencode)")
    ap.add_argument("--no-claude-code", action="store_true",
                    help="leave Claude Code alone, for setting up only the other clients")
    ap.add_argument("--yes", action="store_true", help="register without asking first")
    ap.add_argument("--no-register", action="store_true", help="install without touching any config")
    ap.add_argument("--dry-run", action="store_true", help="print the steps without running them")
    args = ap.parse_args()
    DRY = args.dry_run

    root = os.path.abspath(os.path.expanduser(args.dir))
    only = args.only or list(SERVERS)
    try:
        commands = install(root, only, args.python)
    except subprocess.CalledProcessError as exc:
        sys.exit(f"\nfailed: {' '.join(exc.cmd)}\nnothing was registered; fix the error above and run again")

    if not args.no_register:
        steps = plan(commands, targets(args))
        if not any(new for _, new, _ in steps):
            say("\nevery server is already registered; config not touched")
        elif DRY or confirm(steps, args.yes):
            stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            say("\nbacking up")
            for target, new, _ in steps:
                if new:
                    backup(target.path, stamp)
            for target, new, _ in steps:
                if not new:
                    continue
                say(f"\n{target.label}")
                target.add(new)
                for name in new:
                    say(f"  added {name}")
                if target.hint:
                    say(f"  {target.hint}")
        else:
            say("\nnothing registered")

    say("\ndone" + (" (dry run, nothing changed)" if DRY else ""))


if __name__ == "__main__":
    main()
