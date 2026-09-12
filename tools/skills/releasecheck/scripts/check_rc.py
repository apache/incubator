#!/usr/bin/env python3
"""Deterministic checks on an Apache Incubator release candidate.

This does the mechanical part of a release review and nothing else. It
separates two kinds of output:

  fail       a fact that is wrong (checksum mismatch, no DISCLAIMER, no
             "incubating" in the file name). No judgement needed.
  candidate  something a person has to look at (a file with an ASF header
             and a third-party copyright, a GPL string, a bundled jar).
             Most candidates turn out to be fine. Some are why releases
             get a -1. The script cannot tell which.

It never says whether a release should pass.

Usage:
  check_rc.py --url https://dist.apache.org/repos/dist/dev/incubator/<podling>/<rc>/ \
              --podling <podling> --out <workdir>
  check_rc.py --rc-dir <dir with downloaded artifacts> --keys KEYS --out <workdir>

Optional: --tag-dir <git checkout at the release tag> compares the source
archive with version control.

Writes <workdir>/findings.json and <workdir>/findings.md. Standard library
only, plus the gpg binary for signatures.
"""

import argparse
import datetime
import difflib
import functools
import hashlib
import html.parser
import inspect
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.parse
import urllib.request
import zipfile

ARCHIVE_SUFFIXES = (".tar.gz", ".tgz", ".zip", ".tar.bz2", ".tar.xz")
CHECKSUM_SUFFIXES = (".sha512", ".sha256")
WEAK_CHECKSUM_SUFFIXES = (".md5", ".sha1")

BINARY_EXTENSIONS = {
    ".jar", ".class", ".war", ".ear", ".so", ".dll", ".dylib", ".exe", ".a",
    ".o", ".obj", ".lib", ".pyc", ".pyo", ".whl", ".egg", ".bin", ".wasm",
    ".zip", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar", ".tar", ".nupkg",
    ".gem", ".apk", ".aar", ".node", ".pdb",
}
# Not code, but can carry their own licences, so they are listed separately.
MEDIA_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".webp", ".bmp",
    ".ttf", ".otf", ".woff", ".woff2", ".eot", ".pdf", ".mp3", ".mp4",
}
# Documents and data formats. Test fixtures mostly; listed so someone can
# confirm they are data and not compiled code in disguise.
DATA_EXTENSIONS = {
    ".xls", ".xlsx", ".xlsm", ".docx", ".doc", ".pptx", ".ppt", ".ods", ".odt",
    ".parquet", ".orc", ".avro", ".arrow", ".feather", ".db", ".sqlite", ".pcap",
    ".dat", ".npy", ".npz", ".pkl", ".h5", ".hdf5", ".mat",
}
CODE_EXTENSIONS = {
    ".java", ".kt", ".kts", ".scala", ".groovy", ".py", ".js", ".mjs", ".cjs",
    ".ts", ".tsx", ".jsx", ".go", ".rs", ".c", ".h", ".cc", ".cpp", ".cxx",
    ".hpp", ".hh", ".cs", ".rb", ".php", ".sh", ".bash", ".zsh", ".ps1",
    ".sql", ".proto", ".thrift", ".swift", ".m", ".mm", ".lua", ".pl", ".r",
    ".dart", ".zig", ".erl", ".ex", ".exs", ".clj", ".hs", ".ml", ".vue",
    ".css", ".scss", ".less", ".html", ".htm", ".xml", ".yaml", ".yml",
    ".toml", ".gradle", ".cmake", ".mustache", ".hbs", ".j2", ".tf",
}
CODE_FILENAMES = {"Makefile", "Dockerfile", "CMakeLists.txt", "Jenkinsfile"}
# Documentation needs a header too (source header policy FAQ), apart from the
# short informational files the policy exempts.
DOC_EXTENSIONS = {".md", ".mdx", ".rst", ".adoc", ".asciidoc"}
INFORMATIONAL_NAMES = ("README", "CHANGELOG", "CHANGES", "INSTALL", "CONTRIBUTING", "CODE_OF_CONDUCT",
                       "SECURITY", "AUTHORS", "HISTORY", "MIGRATE", "RELEASE", "UPGRADE", "AGENTS", "CLAUDE",
                       "PKG-INFO", "TODO", "MAINTAINERS", "GOVERNANCE", "SUPPORT", "ROADMAP")
VENDOR_DIR_NAMES = {
    "third_party", "third-party", "thirdparty", "3rdparty", "vendor",
    "vendored", "external", "externals", "node_modules", "deps", "contrib",
}
# Compressed files inside a release. Compressed test data is fine; compiled
# code inside it is not, so these are opened and listed rather than flagged.
NESTED_ARCHIVE_EXTENSIONS = {".zip", ".gz", ".tgz", ".bz2", ".xz", ".tar"}
# Zip containers that usually hold compiled code but do not have to. They are
# opened and judged on what is inside, not on the extension.
JAVA_ARCHIVE_EXTENSIONS = {".jar", ".war", ".ear", ".aar"}
COMPILED_EXTENSIONS = BINARY_EXTENSIONS - NESTED_ARCHIVE_EXTENSIONS - {".bin"}
LEGAL_DIR_NAMES = {"licenses", "licences", "license", "licence", "legal", "licenses-binary"}
# What a LICENSE writes where a real component name would go, as in
# "licenses/LICENSE-[project].txt". A path that runs into one of these is a
# worked example for the reader, not a file the archive is meant to contain.
PLACEHOLDER_OPENERS = "[<{(%$*"
HIDDEN_JUNK = {".DS_Store", "Thumbs.db", ".git", ".svn", ".idea", ".vscode"}
# macOS resource-fork sidecars. bsdtar folds them back into extended attributes
# and does not list them, so a reviewer on macOS never sees them; GNU tar and
# Python extract them as real files.
APPLEDOUBLE = "._"

# Where a project records that it already considered a file's missing header.
# Only the top of the tree is searched, and only the first part of each file.
AUDIT_CONFIG_DEPTH = 3
AUDIT_CONFIG_BYTES = 400_000
RAT_PLUGIN = re.compile(r"apache-rat-plugin|org\.apache\.rat", re.I)
RAT_POM_EXCLUDE = re.compile(r"<exclude>(.*?)</exclude>", re.S)
LICENSERC_IGNORE = re.compile(r"^\s*-\s+['\"]?[^\s'\"#][^\r\n]*", re.M)
# "**/*.md", "*.java", "src/**/*.js" - an exclusion covering a whole file type
# rather than named files. Broad when it recurses ("**") or has no directory
# part at all; "docs/*.md" is one directory's markdown and stays narrow.
EXTENSION_GLOB = re.compile(r"^(?P<prefix>.*?)\*\.(?P<ext>\w+)$")
# File types the source header policy applies to. Excluding one of these
# wholesale removes it from the audit; excluding .json, .lock, .iml, .pem and
# the like is routine, because a header does not belong in them.
HEADERED_EXTENSIONS = (CODE_EXTENSIONS | DOC_EXTENSIONS) - {
    ".xml", ".yaml", ".yml", ".toml", ".j2", ".mustache", ".hbs",
}

# A git checkout of the tag does not contain submodule contents unless they
# were fetched, so every file under a submodule path looks like an addition.
GITMODULES_PATH = re.compile(r"^\s*path\s*=\s*(.+?)\s*$", re.M)

ASF_HEADER = re.compile(r"Licensed to the Apache Software Foundation", re.I)
AL2_PHRASE = re.compile(r"Licensed under the Apache License,?\s+Version 2\.0", re.I)
SPDX = re.compile(r"SPDX-License-Identifier:\s*([^\s*/#>-][^\r\n*]*?)\s*(?:\*/|-->|$)", re.M)
COPYRIGHT = re.compile(
    r"^[^\n]*?(?:(?:Copyright\s*(?:\(c\)|©)?|\(c\)|©)\s*[0-9]{4}"
    r"|Copyright\s*(?:\(c\)|©)?\s*(?:The\s+)?[^\n]*?\b(?:Authors|Contributors)\b)[^\n]*$", re.I | re.M)
ASF_COPYRIGHT = re.compile(r"Apache Software Foundation", re.I)

# Strings that point at licences needing a person to look. Each entry is
# (label, regex). Matches are candidates, not verdicts: a README saying
# "we do not accept GPL code" matches too.
LICENSE_SIGNALS = [
    ("GPL/LGPL/AGPL", re.compile(r"\bGNU (?:Affero |Lesser |Library )?General Public License\b|\b(?:A|L)?GPL-?[23](?:\.0|\.1)?\b|\bGPLv[23]\b", re.I)),
    ("SSPL", re.compile(r"Server Side Public License|\bSSPL\b", re.I)),
    ("BSL/BUSL", re.compile(r"Business Source License|\bBUSL-1\.1\b", re.I)),
    ("Commons Clause", re.compile(r"Commons Clause", re.I)),
    ("Elastic License", re.compile(r"Elastic License", re.I)),
    ("JSON licence", re.compile(r"shall be used for Good, not Evil", re.I)),
    ("Non-commercial", re.compile(r"NonCommercial|\bCC[- ]BY[- ]NC\b", re.I)),
    ("BSD advertising clause", re.compile(r"All advertising materials mentioning features", re.I)),
    ("Category B (MPL/EPL/CDDL)", re.compile(r"Mozilla Public License|Eclipse Public License|\bCDDL\b|Common Development and Distribution License", re.I)),
    ("Dual licence", re.compile(r"\b(?:dual[- ]licen[sc]ed|MIT\s+(?:or|OR|/)\s+GPL|GPL\s+(?:or|OR|/)\s+MIT)\b", re.I)),
]

# Conventional (not mandated) markers of the source archive in its name.
SOURCE_NAME = re.compile(r"[-._](?:src|source)[-._]", re.I)
# A preserved banner or licence tag after an ASF header usually means a
# third-party file (Bootstrap, normalize.css, Font Awesome...) was relabelled.
BANNER = re.compile(
    r"/\*![^0-9]|@license\b|@preserve\b|\bnormalize\.css\b|\bBootstrap v\d|\bFont Awesome\b|"
    r"\bMIT Licen[sc]e\b|\bSIL OFL\b|\bBSD Licen[sc]e\b|\bby @\w+\b", re.I)
# A comment in a code file saying the code came from somewhere else. Most
# are harmless; some are the only trace of a replaced third-party header.
# The source has to look like a project: a link, a quoted or capitalised
# name, or a name followed by a version or the word crate/library/project.
PROVENANCE = re.compile(
    r"\b(?:derived|adapted|ported|copied|forked|borrowed|taken|imported|vendored)\s+from\s+(?:the\s+)?"
    r"(?:\[|`|\"|'|https?://|[A-Z][\w.-]*|[\w.-]+\s+(?:v?\d|`|crate|library|project|package|module))|"
    r"\bbased on the\s+[`'\"\w.-]+\s+(?:crate|library|project|package|module|implementation)\b")
# Banners live in web assets; a "/*!" preserved comment is a banner anywhere.
WEB_EXTENSIONS = {".css", ".scss", ".less", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".html", ".htm", ".vue", ".svg"}
# Canonical Apache License 2.0 text; the copy next to the skill is used first.
AL2_CANONICAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references",
                                  "apache-license-2.0.txt")
AL2_CANONICAL_URL = "https://www.apache.org/licenses/LICENSE-2.0.txt"

NOTICE_LICENSE_TEXT = re.compile(
    r"Permission is hereby granted|Redistribution and use in source and binary forms|"
    r"THE SOFTWARE IS PROVIDED \"AS IS\"|Licensed under the|TERMS AND CONDITIONS", re.I)

MAX_TEXT_BYTES = 2_000_000  # skip scanning huge text blobs
HEAD_LINES = 60             # where headers are looked for
EXAMPLES = 15               # examples per bucket in the markdown summary


# ---------------------------------------------------------------- download

class _Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.hrefs.append(v)


def _get(url, dest=None):
    req = urllib.request.Request(url, headers={"User-Agent": "podling-release-check"})
    with urllib.request.urlopen(req, timeout=120) as r:
        if dest is None:
            return r.read()
        with open(dest, "wb") as f:
            shutil.copyfileobj(r, f)
    return None


def fetch_rc(url, dest):
    """Download every file listed in an svn/dist directory listing."""
    if not url.endswith("/"):
        url += "/"
    page = _get(url).decode("utf-8", "replace")
    p = _Links()
    p.feed(page)
    names = []
    for h in p.hrefs:
        if h.startswith(("?", "#", "/", "..")) or h.endswith("/") or "://" in h:
            continue
        name = urllib.parse.unquote(h)
        if "/" in name or name in names:
            continue
        names.append(name)
    os.makedirs(dest, exist_ok=True)
    for n in names:
        _get(url + urllib.parse.quote(n), os.path.join(dest, n))
    return names


# ---------------------------------------------------------------- helpers

class Findings:
    def __init__(self):
        self.items = []

    def add(self, kind, check, message, path=None, evidence=None):
        self.items.append({"kind": kind, "check": check, "message": message,
                           "path": path, "evidence": evidence})

    def fail(self, *a, **k):
        self.add("fail", *a, **k)

    def candidate(self, *a, **k):
        self.add("candidate", *a, **k)

    def ok(self, *a, **k):
        self.add("ok", *a, **k)

    def info(self, *a, **k):
        self.add("info", *a, **k)


def is_archive(name):
    return name.endswith(ARCHIVE_SUFFIXES)


def read_text(path):
    try:
        if os.path.getsize(path) > MAX_TEXT_BYTES:
            return None
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return None
    if b"\0" in data[:8192]:
        return None
    return data.decode("utf-8", "replace")


def looks_binary(path):
    try:
        with open(path, "rb") as f:
            return b"\0" in f.read(8192)
    except OSError:
        return False


# Magic numbers for compiled code: ELF, Java class (also Mach-O fat), Mach-O,
# Windows PE, WebAssembly.
COMPILED_MAGIC = (b"\x7fELF", b"\xca\xfe\xba\xbe", b"\xcf\xfa\xed\xfe", b"\xce\xfa\xed\xfe", b"\x00asm")


def is_compiled_bytes(head):
    return head.startswith(COMPILED_MAGIC) or (head[:2] == b"MZ" and b"\0" in head[:64])


def inspect_nested(path):
    """List an archive found inside the release without extracting it.

    Returns (compiled_entries, entry_count, error). A single-file .gz is
    decompressed in memory and sniffed for binary content.
    """
    compiled = []
    try:
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path) as z:
                names = [i.filename for i in z.infolist() if not i.is_dir()]
                for n in names:
                    if os.path.splitext(n.lower())[1] in COMPILED_EXTENSIONS:
                        compiled.append(n)
                return compiled, len(names), None
        if tarfile.is_tarfile(path):
            with tarfile.open(path) as t:
                count = 0
                for m in t:
                    if not m.isfile():
                        continue
                    count += 1
                    if os.path.splitext(m.name.lower())[1] in COMPILED_EXTENSIONS:
                        compiled.append(m.name)
                        continue
                    fh = t.extractfile(m)
                    head = fh.read(8192) if fh else b""
                    if is_compiled_bytes(head):
                        compiled.append(m.name)
                return compiled, count, None
        import bz2
        import gzip
        import lzma
        opener = {".gz": gzip.open, ".bz2": bz2.open, ".xz": lzma.open}.get(os.path.splitext(path.lower())[1])
        if opener:
            with opener(path, "rb") as fh:
                head = fh.read(8192)
            if is_compiled_bytes(head):
                compiled.append(os.path.basename(path))
            return compiled, 1, None
        return [], 0, "not a recognised archive format"
    except Exception as e:  # noqa: BLE001
        return [], 0, str(e)


def safe_extract(archive, dest):
    """Extract, refusing absolute paths, .. traversal and links out of dest."""
    dest = os.path.realpath(dest)
    os.makedirs(dest, exist_ok=True)

    def inside(p):
        full = os.path.realpath(os.path.join(dest, p))
        return full == dest or full.startswith(dest + os.sep)

    if archive.endswith(".zip"):
        with zipfile.ZipFile(archive) as z:
            for m in z.namelist():
                if not inside(m):
                    raise ValueError(f"unsafe path in archive: {m}")
            z.extractall(dest)
    else:
        with tarfile.open(archive) as t:
            members = []
            for m in t.getmembers():
                if not inside(m.name):
                    raise ValueError(f"unsafe path in archive: {m.name}")
                if m.issym() or m.islnk():
                    if not inside(os.path.join(os.path.dirname(m.name), m.linkname)):
                        raise ValueError(f"link escapes archive: {m.name}")
                if m.isdev():
                    continue
                members.append(m)
            if "filter" in inspect.signature(t.extractall).parameters:
                t.extractall(dest, members=members, filter="data")
            else:
                t.extractall(dest, members=members)
    return dest


def top_dir(extracted):
    """The directory the release really unpacks into.

    Some archives nest twice, "Apache-SDAP/apache-sdap-1.2.0-src/...", so the
    first level holds nothing but another directory and the legal files are
    one deeper. Reporting LICENSE, NOTICE and DISCLAIMER as missing in that
    case is wrong, so keep descending while the level holds only a single
    directory. Bounded, so a pathological archive cannot walk far.
    """
    root, name = extracted, None
    for _ in range(4):
        entries = [e for e in os.listdir(root)
                   if e not in HIDDEN_JUNK and not e.startswith(APPLEDOUBLE)]
        if len(entries) != 1 or not os.path.isdir(os.path.join(root, entries[0])):
            break
        root, name = os.path.join(root, entries[0]), entries[0]
    return root, name


# ---------------------------------------------------------------- artifact checks

def check_checksum(artifact, f):
    base = os.path.basename(artifact)
    found = False
    for suf in CHECKSUM_SUFFIXES:
        side = artifact + suf
        if not os.path.exists(side):
            continue
        found = True
        algo = "sha512" if suf == ".sha512" else "sha256"
        h = hashlib.new(algo)
        with open(artifact, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        with open(side, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        # Accept "hash  file", "hash *file" and the gpg --print-md layout,
        # which splits the hash into space-separated groups over lines.
        size = 128 if algo == "sha512" else 64
        compact = re.sub(r"[^0-9a-fA-F]", "", text.split(":", 1)[-1]) if ":" in text.split("\n")[0] else None
        m = re.search(r"\b[0-9a-fA-F]{%d}\b" % size, text)
        want = (m.group(0) if m else (compact or "")[:size]).lower()
        if want == h.hexdigest():
            f.ok("checksum", f"{algo} matches", path=base)
        else:
            f.fail("checksum", f"{algo} does not match", path=base,
                   evidence={"expected": want or text.strip()[:200], "actual": h.hexdigest()})
    for suf in WEAK_CHECKSUM_SUFFIXES:
        if os.path.exists(artifact + suf):
            f.candidate("checksum", f"{suf[1:]} checksum present; release distribution policy says SHA-256/512 and not MD5/SHA-1",
                        path=base)
    if not found:
        f.fail("checksum", "no .sha512 or .sha256 file", path=base)


def find_keys(args, rc_dir, f):
    """Locate the KEYS file: --keys, else the release area, else dist/dev, else the RC directory.

    Release distribution policy wants KEYS in the release area, so using a
    fallback is reported as a candidate. Returns a local path or None.
    """
    candidates = []
    if args.keys:
        candidates.append((args.keys, None))
    if args.podling:
        # Tried even when --keys was given, so one dead URL does not stop the
        # signature check. A podling that has since graduated no longer has a
        # KEYS under incubator/: it moves to its own name, and the copy that
        # was live during the vote stays in the archive.
        candidates.append((f"https://downloads.apache.org/incubator/{args.podling}/KEYS", None))
        candidates.append((f"https://dist.apache.org/repos/dist/dev/incubator/{args.podling}/KEYS",
                           "KEYS found in dist/dev but not in the release area (downloads.apache.org)"))
        candidates.append((f"https://archive.apache.org/dist/incubator/{args.podling}/KEYS",
                           "KEYS found only in the archive; the release area no longer serves it"))
        candidates.append((f"https://downloads.apache.org/{args.podling}/KEYS",
                           "KEYS found under the project's own name, not under incubator/"))
    local = os.path.join(rc_dir, "KEYS")
    if os.path.exists(local):
        candidates.append((local, "KEYS taken from the RC directory itself, not the release area"))
    errors, found = [], []
    for n, (src, note) in enumerate(candidates):
        if src.startswith(("http://", "https://")):
            # A distinct file per source, so a later fetch cannot overwrite an
            # earlier one before both have been read.
            path = os.path.join(args.out, "KEYS" if n == 0 else f"KEYS.{n}")
            try:
                _get(src, path)
            except Exception as e:  # noqa: BLE001 - try the next location
                errors.append(f"{src}: {e}")
                continue
        else:
            path = src
        found.append((src, path, note))
    if not found:
        if candidates:
            f.fail("signature", "could not fetch KEYS", evidence=errors)
        return None
    # Every reachable KEYS is used, not just the first. A podling's release
    # area, its dist/dev area and the archive can each hold a different set,
    # and a release manager's key is sometimes in only one of them. Stopping
    # at the first reachable file reports a good signature as unverifiable.
    src, path, note = found[0]
    f.info("signature", f"KEYS used: {src}")
    if note:
        f.candidate("signature", note, evidence=src)
    if len(found) > 1:
        merged = os.path.join(args.out, "KEYS-merged")
        with open(merged, "wb") as out:
            for s, p, _ in found:
                try:
                    with open(p, "rb") as fh:
                        out.write(fh.read())
                        out.write(b"\n")
                except OSError:
                    continue
        f.info("signature", "keys from every reachable KEYS location were merged for verification",
               evidence=[s for s, _, _ in found])
        return merged
    return path


def gpg_home(keys_path):
    home = tempfile.mkdtemp(prefix="rc-gpg-")
    os.chmod(home, 0o700)
    subprocess.run(["gpg", "--homedir", home, "--batch", "--quiet", "--import", keys_path],
                   capture_output=True, check=False)
    return home


def check_signature(artifact, home, f):
    base = os.path.basename(artifact)
    sig = artifact + ".asc"
    if not os.path.exists(sig):
        f.fail("signature", "no .asc signature", path=base)
        return
    if home is None:
        f.candidate("signature", "signature present but not verified (no KEYS file)", path=base)
        return
    r = subprocess.run(["gpg", "--homedir", home, "--batch", "--status-fd", "1",
                        "--verify", sig, artifact], capture_output=True, text=True)
    status = r.stdout
    good = re.search(r"\[GNUPG:\] GOODSIG (\S+) (.*)", status)
    valid = re.search(r"\[GNUPG:\] VALIDSIG (\S+)", status)
    if good and valid:
        uid = good.group(2).strip()
        f.ok("signature", "good signature from a key in KEYS", path=base,
             evidence={"fingerprint": valid.group(1), "uid": uid})
        if "@apache.org" not in uid:
            f.info("signature", "signing key uid has no @apache.org address (not a policy failure)",
                   path=base, evidence={"uid": uid})
    elif "NO_PUBKEY" in status:
        f.fail("signature", "signing key is not in KEYS", path=base,
               evidence=re.findall(r"NO_PUBKEY (\S+)", status))
    elif "EXPKEYSIG" in status:
        # gpg judges expiry against now. A key that expired after the vote
        # signed a valid signature at the time, so reporting a blocker would
        # fail every older release whose signer has since let a key lapse.
        made, expires = sig_and_expiry(status)
        ev = {"key": re.findall(r"EXPKEYSIG (\S+ .*)", status),
              "signed": made, "key_expired": expires}
        if made and expires and made < expires:
            f.candidate("signature", "signature is good and was made before the key expired; the key "
                                     "has expired since", path=base, evidence=ev)
        else:
            f.fail("signature", "signature made with a key that was already expired", path=base,
                   evidence=ev)
    elif "REVKEYSIG" in status:
        f.fail("signature", "signature made with a key that is revoked in KEYS", path=base,
               evidence=re.findall(r"REVKEYSIG (\S+ .*)", status))
    else:
        f.fail("signature", "signature does not verify", path=base,
               evidence=(status or r.stderr)[-500:])


def sig_and_expiry(status):
    """When the signature was made, and when the key expired, as epoch ints.

    gpg's status output carries both: SIG_CREATED is absent on verify, but
    VALIDSIG and EXPKEYSIG carry timestamps, and KEYEXPIRED gives the expiry.
    Either may be missing, in which case the caller cannot compare them.
    """
    made = expires = None
    # VALIDSIG <fingerprint> <date> <sig-epoch> ...
    m = re.search(r"\[GNUPG:\] VALIDSIG \S+ \S+ (\d{9,})", status)
    k = re.search(r"\[GNUPG:\] KEYEXPIRED (\d{9,})", status)
    if m:
        made = int(m.group(1))
    if k:
        expires = int(k.group(1))
    return made, expires


# ---------------------------------------------------------------- content checks

def normalise(text):
    """Lower case, straight quotes, hyphens as spaces, collapsed whitespace."""
    text = text.lower().replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"[-\u2010-\u2014]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def compare_disclaimer(text, template):
    """Check the fixed parts of a disclaimer template appear, in order.

    Placeholders in the template are written as {} or {anything}. Returns the
    fixed fragments that are missing.
    """
    body = normalise(text)
    missing = []
    pos = 0
    for frag in re.split(r"\{[^}]*\}", template):
        frag = normalise(frag)
        if len(frag) < 4:
            continue
        i = body.find(frag, pos)
        if i < 0:
            missing.append(frag)
        else:
            pos = i + len(frag)
    return missing


def wip_issue_list(text):
    """Text between the known-issues sentence and the licensing review sentence."""
    m = re.search(r"likely to be incomplete\)\s*:?(.*?)if you are planning", normalise(text), re.S)
    return None if m is None else m.group(1).strip()


@functools.lru_cache(maxsize=1)
def canonical_al2():
    """The canonical Apache License 2.0 text, or None if it cannot be read."""
    try:
        with open(AL2_CANONICAL_PATH, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        pass
    try:
        return _get(AL2_CANONICAL_URL).decode("utf-8", "replace")
    except Exception:  # noqa: BLE001 - offline; the caller reports it
        return None


def _al2_lines(text):
    """The licence terms (sections 1-9) as normalised non-empty lines.

    The appendix is fill-in instructions, not terms, and copies differ in
    trivial ways ("[yyyy]" vs "{yyyy}"), so it is left out.
    """
    out = []
    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line.replace("https://", "http://")).strip()
        if line:
            out.append(line)
    end = next((i for i, line in enumerate(out) if "END OF TERMS AND CONDITIONS" in line), None)
    return out[:end + 1] if end is not None else out


def disclaimer_stem(name):
    """DISCLAIMER-WIP.txt -> DISCLAIMER-WIP; disclaimer.md -> DISCLAIMER."""
    stem = name.upper()
    for ext in (".TXT", ".MD", ".RST"):
        if stem.endswith(ext):
            stem = stem[:-len(ext)]
            break
    return stem


def compare_al2(text):
    """Lines where the Apache License terms differ from the canonical copy; None if not comparable."""
    canon = canonical_al2()
    if canon is None:
        return None
    return [d for d in difflib.unified_diff(_al2_lines(canon), _al2_lines(text), lineterm="", n=0)
            if d[:1] in "+-" and not d.startswith(("+++", "---"))]


def check_root_files(root, label, rc_year, f, templates=None):
    templates = templates or {}
    names = set(os.listdir(root))
    for req in ("LICENSE", "NOTICE"):
        hits = [n for n in names if n == req or n.startswith(req + ".")]
        if hits:
            f.ok("root-files", f"{req} present", path=f"{label}/{hits[0]}")
        else:
            f.fail("root-files", f"no {req} file at the top level", path=label)

    # Only DISCLAIMER and DISCLAIMER-WIP carry the incubation disclaimer.
    # A project may ship other DISCLAIMER-<topic> documents, such as a
    # DISCLAIMER-BINARIES listing test fixtures, and holding those to the
    # incubation wording reports a fact that is not true.
    disc = [n for n in names if disclaimer_stem(n) in ("DISCLAIMER", "DISCLAIMER-WIP")]
    other = [n for n in names if n.upper().startswith("DISCLAIMER") and n not in disc]
    if not disc:
        f.fail("disclaimer", "no DISCLAIMER or DISCLAIMER-WIP file at the top level", path=label)
    if other:
        f.info("disclaimer", "other DISCLAIMER-named files, not checked as the incubation disclaimer",
               path=label, evidence=sorted(other))
    for d in disc:
        text = read_text(os.path.join(root, d)) or ""
        if not re.search(r"incubat", text, re.I):
            f.fail("disclaimer", f"{d} does not mention incubation", path=f"{label}/{d}")
        else:
            f.ok("disclaimer", f"{d} present and mentions incubation", path=f"{label}/{d}")
        kind = "wip" if "WIP" in d.upper() else "standard"
        template = templates.get(kind)
        if template is None:
            f.candidate("disclaimer", f"{d} not compared with the standard text (no template given)",
                        path=f"{label}/{d}", evidence=text[:600])
        else:
            missing = compare_disclaimer(text, template)
            if missing:
                f.candidate("disclaimer",
                            f"{d} differs from the {kind} disclaimer text; other wording needs IPMC approval",
                            path=f"{label}/{d}", evidence=missing[:5])
            else:
                f.ok("disclaimer", f"{d} matches the {kind} disclaimer text", path=f"{label}/{d}")
        if kind == "wip":
            issues = wip_issue_list(text)
            if issues is None:
                f.candidate("disclaimer", "DISCLAIMER-WIP: could not find the list of known issues",
                            path=f"{label}/{d}")
            elif len(issues) < 10 or "list of known issues goes here" in issues:
                f.candidate("disclaimer", "DISCLAIMER-WIP: the list of known issues is empty or still the placeholder",
                            path=f"{label}/{d}", evidence=issues[:300])
            else:
                f.info("disclaimer", "DISCLAIMER-WIP known issues, for review", path=f"{label}/{d}",
                       evidence=issues[:1500])

    notice = next((n for n in names if n == "NOTICE" or n.startswith("NOTICE.")), None)
    if notice:
        text = read_text(os.path.join(root, notice)) or ""
        years = [int(y) for y in re.findall(r"\b(19[89]\d|20\d\d)\b", text[:2000])]
        if not ASF_COPYRIGHT.search(text[:1000]):
            f.candidate("notice", "no ASF copyright line near the top of NOTICE", path=f"{label}/{notice}",
                        evidence=text[:300])
        if years and max(years) < rc_year:
            f.candidate("notice", f"NOTICE copyright year {max(years)} is before {rc_year}",
                        path=f"{label}/{notice}", evidence=text[:300])
        m = NOTICE_LICENSE_TEXT.search(text)
        if m:
            f.candidate("notice", "NOTICE appears to contain licence text; licences belong in LICENSE",
                        path=f"{label}/{notice}", evidence=text[max(0, m.start() - 150):m.end() + 150])
        f.info("notice", "NOTICE text for review", path=f"{label}/{notice}", evidence=text[:4000])

    lic = next((n for n in names if n == "LICENSE" or n.startswith("LICENSE.")), None)
    if lic:
        text = read_text(os.path.join(root, lic)) or ""
        if "Apache License" not in text[:400] or "Version 2.0" not in text[:600]:
            f.fail("license", "LICENSE does not start with the Apache License 2.0 text", path=f"{label}/{lic}")
        else:
            diffs = compare_al2(text)
            if diffs is None:
                f.info("license-text", "Apache License text not compared: canonical text unavailable",
                       path=f"{label}/{lic}")
            elif diffs:
                f.fail("license-text", "Apache License 2.0 text in LICENSE differs from the canonical text",
                       path=f"{label}/{lic}", evidence=diffs[:12])
            else:
                f.ok("license-text", "Apache License 2.0 text matches the canonical text", path=f"{label}/{lic}")
        # Anything after the AL2 appendix is a third-party section. The phrase
        # "limitations under the License." occurs once in the canonical text,
        # in the appendix, so look for it after the end of the terms.
        end = text.find("END OF TERMS AND CONDITIONS")
        tail = text[end:] if end >= 0 else text
        k = tail.find("limitations under the License.")
        extra = tail[k + len("limitations under the License."):].strip() if k >= 0 else ""
        f.info("license", "third-party sections appended to LICENSE" if extra else
               "LICENSE is the plain Apache License with nothing appended",
               path=f"{label}/{lic}", evidence=extra[:4000] if extra else None)
        # Pointers to licence files that should exist in the archive.
        # Not preceded by "/" so URLs such as apache.org/licenses/LICENSE-2.0 are skipped.
        missing = []
        # The lookbehind excludes "-" so that a path under "ui-licenses/" is
        # not read as a path under "licenses/", and "/" so that a URL such as
        # apache.org/licenses/LICENSE-2.0 is skipped.
        for m in re.finditer(r"(?<![\w/.\-])((?:licenses?|licences?|LICENSES?)/[\w.\-/]+)", text):
            ref = m.group(1)
            # "licenses/LICENSE-[project].txt" and similar are instructions to
            # the reader, not paths. The name is cut short at the placeholder,
            # so the truncated stem would always look like a missing file.
            if text[m.end():m.end() + 1] in PLACEHOLDER_OPENERS or ref.rstrip(".")[-1] in "-_/":
                continue
            if os.path.exists(os.path.join(root, ref.rstrip("."))):
                continue
            missing.append(ref)
        for ref in sorted(set(missing)):
            f.fail("license", "LICENSE points to a file that is not in the archive", path=f"{label}/{lic}",
                   evidence=ref)
        # Walk the legal directories that are actually in the archive. Probing
        # a list of spellings reports every file twice on a case-insensitive
        # filesystem, where "licenses" and "LICENSES" are the same directory.
        for d in sorted(n for n in os.listdir(root)
                        if n.lower() in LEGAL_DIR_NAMES and os.path.isdir(os.path.join(root, n))):
            for n in sorted(os.listdir(os.path.join(root, d))):
                if n.startswith(APPLEDOUBLE):
                    continue  # reported once, with a count, as junk
                if f"{d}/{n}" not in text and n not in text:
                    f.candidate("license", "licence file not referenced from LICENSE",
                                path=f"{label}/{d}/{n}")


def classify_header(head):
    has_asf = bool(ASF_HEADER.search(head))
    has_al2 = bool(AL2_PHRASE.search(head))
    spdx = [s.strip() for s in SPDX.findall(head)]
    copyrights = [c.strip() for c in COPYRIGHT.findall(head)]
    foreign = [c for c in copyrights if not ASF_COPYRIGHT.search(c)]
    return has_asf, has_al2, spdx, foreign


def scan_tree(root, label, f, stats):
    appledouble = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        for d in list(dirnames):
            if d in HIDDEN_JUNK:
                f.candidate("junk", "unexpected directory in release", path=f"{label}/{os.path.join(rel_dir, d)}")
                dirnames.remove(d)
            elif d.lower() in VENDOR_DIR_NAMES:
                f.candidate("vendored", "vendored/third-party directory; check each component is in LICENSE",
                            path=f"{label}/{os.path.normpath(os.path.join(rel_dir, d))}")
        for name in filenames:
            full = os.path.join(dirpath, name)
            rel = os.path.normpath(os.path.join(rel_dir, name))
            shown = f"{label}/{rel}"
            stats["files"] += 1
            if os.path.islink(full):
                continue
            if name in HIDDEN_JUNK:
                f.candidate("junk", "unexpected file in release", path=shown)
                continue
            if name.startswith(APPLEDOUBLE):
                appledouble.append(rel)
                continue
            lower = name.lower()
            ext = os.path.splitext(lower)[1]
            if ext == ".bin" and not looks_binary(full):
                ext = ""  # named .bin but plain text; scan it like any other file
            if ext in NESTED_ARCHIVE_EXTENSIONS or lower.endswith((".tar.gz", ".tar.bz2", ".tar.xz")):
                compiled, total, err = inspect_nested(full)
                if err:
                    f.candidate("binary", "archive inside the release that could not be read", path=shown, evidence=err)
                elif compiled:
                    f.candidate("binary", "archive inside the release contains compiled or binary files",
                                path=shown, evidence=compiled[:10])
                else:
                    f.candidate("nested-archive",
                                f"compressed file with no compiled code in it ({total} entries); usually test data",
                                path=shown)
                stats["binary"] += 1 if compiled or err else 0
                stats["nested_archive"] += 1
                continue
            if ext in JAVA_ARCHIVE_EXTENSIONS:
                # A named build wrapper jar is compiled code by definition, so
                # it is a fact rather than something for a person to weigh. A
                # source release cannot contain compiled code. Every other jar
                # is opened before it is judged: a Java project's test tree is
                # full of fixtures like an empty.jar or a jar of resources,
                # which carry no compiled code and are not a policy problem.
                compiled, total, err = inspect_nested(full)
                if name in ("gradle-wrapper.jar", "maven-wrapper.jar"):
                    f.fail("binary", "build wrapper jar in source release; a source release cannot "
                                     "contain compiled code", path=shown, evidence=(compiled or [])[:10])
                elif err:
                    f.candidate("binary", f"{ext[1:]} in the release that could not be read",
                                path=shown, evidence=err)
                elif compiled:
                    f.candidate("binary", f"{ext[1:]} in source release containing compiled code "
                                          f"({len(compiled)} of {total} entries)",
                                path=shown, evidence=compiled[:10])
                else:
                    f.candidate("nested-archive",
                                f"{ext[1:]} with no compiled code in it ({total} entries); "
                                "usually a test fixture", path=shown)
                stats["binary"] += 1 if compiled or err else 0
                stats["nested_archive"] += 1
                continue
            if ext in BINARY_EXTENSIONS:
                f.candidate("binary", "binary file in source release", path=shown)
                stats["binary"] += 1
                continue
            if ext in MEDIA_EXTENSIONS:
                stats["media"] += 1
                f.add("media", "media", "image/font/document; may carry its own licence", path=shown)
                continue
            if ext in DATA_EXTENSIONS:
                stats["data"] += 1
                f.add("data", "data", "document or data file; usually test data", path=shown)
                continue
            text = read_text(full)
            if text is None:
                if looks_binary(full):
                    f.candidate("binary", "file with binary content", path=shown)
                    stats["binary"] += 1
                continue

            head = "\n".join(text.splitlines()[:HEAD_LINES])
            has_asf, has_al2, spdx, foreign = classify_header(head)
            is_code = ext in CODE_EXTENSIONS or name in CODE_FILENAMES
            is_doc = (ext in DOC_EXTENSIONS and not name.upper().startswith(INFORMATIONAL_NAMES)
                      and not rel.startswith(".github"))
            legal = (name.upper().startswith(("LICENSE", "LICENCE", "NOTICE", "COPYING", "DISCLAIMER"))
                     or any(part.lower() in LEGAL_DIR_NAMES for part in rel.split(os.sep)[:-1]))

            if legal:
                pass  # LICENSE, NOTICE and bundled licence texts are checked in check_root_files
            elif has_asf and foreign:
                f.candidate("header-provenance",
                            "ASF header together with a non-ASF copyright line: may be third-party code relabelled",
                            path=shown, evidence=foreign[:3])
                stats["asf_plus_foreign"] += 1
            elif has_asf:
                banner = BANNER.search(head[ASF_HEADER.search(head).end():])
                if banner and not banner.group(0).startswith("/*!") and ext not in WEB_EXTENSIONS:
                    banner = None
                if banner:
                    line = next((l for l in head.splitlines() if banner.group(0) in l), banner.group(0))
                    f.candidate("header-provenance",
                                "ASF header followed by a third-party banner or licence tag: may be third-party code relabelled",
                                path=shown, evidence=[line.strip()[:200]])
                    stats["asf_plus_foreign"] += 1
                else:
                    stats["asf_header"] += 1
            elif spdx:
                non_al2 = [s for s in spdx if s != "Apache-2.0"]
                if non_al2:
                    f.candidate("header-other-licence", "SPDX identifier for a licence other than Apache-2.0",
                                path=shown, evidence=non_al2)
                else:
                    f.candidate("header-spdx-only",
                                "SPDX Apache-2.0 line without the ASF header text; check current source header policy",
                                path=shown)
                stats["spdx"] += 1
            elif has_al2 or foreign:
                f.candidate("header-third-party",
                            "third-party header (Apache-licensed or other copyright); check LICENSE and NOTICE cover it",
                            path=shown, evidence=foreign[:3] or ["Licensed under the Apache License 2.0 (not ASF)"])
                stats["third_party_header"] += 1
            elif is_code:
                f.add("no-header", "no-header", "no licence header", path=shown)
                stats["no_header"] += 1
            elif is_doc:
                f.add("no-header", "no-header", "documentation file with no licence header", path=shown)
                stats["no_header"] += 1

            for label_, rx in LICENSE_SIGNALS:
                m = rx.search(text)
                if m:
                    s = max(0, m.start() - 120)
                    f.candidate("licence-signal", f"mentions {label_}", path=shown,
                                evidence=text[s:m.end() + 120].replace("\n", " "))
                    stats["licence_signal"] += 1
                    break
            if is_code and not legal and not foreign and not has_al2:
                m = PROVENANCE.search(text)
                if m:
                    s = max(0, m.start() - 100)
                    f.candidate("provenance-note",
                                "says code was derived, adapted, ported or copied from elsewhere; check LICENSE covers it",
                                path=shown, evidence=text[s:m.end() + 140].replace("\n", " "))

    if appledouble:
        stats["appledouble"] = stats.get("appledouble", 0) + len(appledouble)
        f.candidate("junk", f"macOS AppleDouble sidecar files in the release ({len(appledouble)}); "
                            "bsdtar hides them, so they are invisible to a reviewer on macOS",
                    path=label, evidence=sorted(appledouble)[:10])

    licence_audit_config(root, label, f)


def licence_audit_config(root, label, f):
    """Find the project's own licence-header audit configuration.

    A missing ASF header only matters when nobody has already considered the
    file. Projects record that decision in a RAT exclude list, and the list is
    not always in `.rat-excludes`: the apache-rat Maven plugin keeps it in a
    `pom.xml`, and skywalking-eyes keeps it in `.licenserc.yaml`. Reporting a
    header count without saying the project excluded those paths, and that the
    reviewers who ran RAT therefore saw nothing, produces false blockers.
    """
    found, broad = [], []
    for dirpath, dirnames, filenames in os.walk(root):
        for d in list(dirnames):
            if d in HIDDEN_JUNK or d.lower() in VENDOR_DIR_NAMES:
                dirnames.remove(d)
        rel_dir = os.path.relpath(dirpath, root)
        depth = 0 if rel_dir == "." else rel_dir.count(os.sep) + 1
        if depth > AUDIT_CONFIG_DEPTH:
            dirnames[:] = []
            continue
        for name in filenames:
            rel = os.path.normpath(os.path.join(rel_dir, name))
            low = name.lower()
            patterns = None
            if low in (".rat-excludes", "rat-excludes"):
                patterns = read_lines(os.path.join(dirpath, name))
            elif low in (".licenserc.yaml", ".licenserc.yml", "licenserc.toml", ".licenserc.json"):
                patterns = read_matches(os.path.join(dirpath, name), LICENSERC_IGNORE)
            elif low == "pom.xml":
                patterns = read_matches(os.path.join(dirpath, name), RAT_POM_EXCLUDE, needs=RAT_PLUGIN)
            if patterns:
                found.append(f"{rel} ({len(patterns)} excluded paths)")
                for pat in broad_excludes(patterns):
                    broad.append(f"{rel}: {pat}")
    if found:
        f.info("no-header", "the archive carries its own licence-audit configuration; a path excluded "
                            "there is the project saying it already considered the header question",
               path=label, evidence=sorted(found)[:20])
    if broad:
        f.candidate("no-header", f"the licence-audit configuration excludes whole classes of source or "
                                 f"documentation ({len(broad)} patterns); a clean RAT run does not mean "
                                 "those files were looked at",
                    path=label, evidence=sorted(set(broad))[:25])


def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return [ln.strip() for ln in fh if ln.strip() and not ln.lstrip().startswith("#")]
    except OSError:
        return []


def read_matches(path, pattern, needs=None):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read(AUDIT_CONFIG_BYTES)
    except OSError:
        return []
    if needs is not None and not needs.search(text):
        return []
    out = []
    for m in pattern.findall(text):
        s = (m if isinstance(m, str) else m[0]).strip()
        s = re.sub(r"^-\s+", "", s).strip().strip("'\"").strip()
        if s:
            out.append(s)
    return out


def broad_excludes(patterns):
    """Exclusions that sweep whole classes of file the header policy covers.

    A project can make RAT pass by excluding everything. "**/*.md" or
    "**/*.js" is not a decision about particular files, it removes a whole
    language or all the documentation from the audit, so a clean RAT run says
    nothing about them. Data, lock, IDE and credential files are different:
    a header does not belong in them, and excluding those is routine.
    """
    out = []
    for pat in patterns:
        p = pat.strip().strip("/")
        if p in ("**", "*", ".", "**/*", "./**"):
            out.append(pat)
            continue
        m = EXTENSION_GLOB.match(p)
        if not m or "." + m.group("ext").lower() not in HEADERED_EXTENSIONS:
            continue
        prefix = m.group("prefix")
        if "**" in p or "/" not in prefix:
            out.append(pat)
    return out


def unfetched_submodules(tag_dir):
    """Submodule paths declared in .gitmodules that hold no files."""
    gm = os.path.join(tag_dir, ".gitmodules")
    if not os.path.isfile(gm):
        return set()
    try:
        with open(gm, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read(AUDIT_CONFIG_BYTES)
    except OSError:
        return set()
    out = set()
    for raw in GITMODULES_PATH.findall(text):
        rel = os.path.normpath(raw.strip())
        if rel in (".", os.sep) or rel.startswith(".."):
            continue
        full = os.path.join(tag_dir, rel)
        if not os.path.isdir(full) or not any(fn for _, _, fn in os.walk(full)):
            out.add(rel)
    return out


def under_any(rel, prefixes):
    return any(rel == p or rel.startswith(p + os.sep) for p in prefixes)


def compare_with_tag(root, tag_dir, label, f):
    def listing(base, skip_git):
        out = set()
        for dp, dn, fn in os.walk(base):
            if skip_git and ".git" in dn:
                dn.remove(".git")
            for n in fn:
                full = os.path.join(dp, n)
                if os.path.islink(full) or n.startswith(APPLEDOUBLE):
                    continue  # links are not content; sidecars are reported on their own
                out.add(os.path.normpath(os.path.relpath(full, base)))
        return out

    arc = listing(root, False)
    tag = listing(tag_dir, True)
    # Submodules the checkout never fetched are not files the release added.
    empty_subs = unfetched_submodules(tag_dir)
    if empty_subs:
        hidden = sorted(r for r in arc - tag if under_any(r, empty_subs))
        if hidden:
            arc = {r for r in arc if not under_any(r, empty_subs)}
            f.info("vs-tag", f"{len(hidden)} files under {len(empty_subs)} git submodule path(s) were "
                             "excluded from the comparison; the checkout did not fetch them, so they "
                             "are bundled third-party code to check against LICENSE, not additions",
                   path=label, evidence=sorted(empty_subs))
    only_arc = sorted(arc - tag)
    only_tag = sorted(tag - arc)
    changed = []
    for rel in sorted(arc & tag):
        a, b = os.path.join(root, rel), os.path.join(tag_dir, rel)
        if not (os.path.isfile(a) and os.path.isfile(b)):
            continue  # unreadable or vanished on one side; not a content difference
        if os.path.getsize(a) != os.path.getsize(b):
            changed.append(rel)
        else:
            with open(a, "rb") as x, open(b, "rb") as y:
                if x.read() != y.read():
                    changed.append(rel)
    for rel in only_arc:
        f.candidate("vs-tag", "in the source archive but not in the tag", path=f"{label}/{rel}")
    for rel in changed:
        f.candidate("vs-tag", "differs from the file at the tag", path=f"{label}/{rel}")
    f.info("vs-tag", f"{len(only_tag)} files in the tag are not in the archive (often deliberate)",
           evidence=only_tag[:200])
    # A whole top-level directory left out of the archive is deliberate until
    # the archive's own README, Dockerfile or build files still refer to it.
    tag_dirs = {rel.split(os.sep)[0] for rel in only_tag if os.sep in rel}
    arc_dirs = {rel.split(os.sep)[0] for rel in arc if os.sep in rel}
    refs = {}
    for name in sorted(os.listdir(root)):
        if name.upper().startswith(("README", "DOCKERFILE", "MAKEFILE", "BUILD")) or name in (
                "pom.xml", "settings.gradle", "settings.gradle.kts", "Cargo.toml", "package.json", "CMakeLists.txt"):
            refs[name] = read_text(os.path.join(root, name)) or ""
    for d in sorted(tag_dirs - arc_dirs):
        if d.startswith(".") or len(d) < 4:
            continue
        hits = [n for n, t in refs.items() if re.search(r"(?<![\w-])" + re.escape(d) + r"(?![\w-])", t)]
        if hits:
            f.candidate("vs-tag", "directory in the tag is not in the archive but the archive still refers to it",
                        path=f"{label}/{d}", evidence=hits)


# ---------------------------------------------------------------- report

def holder(evidence):
    """A copyright line with the years and boilerplate removed, for grouping."""
    if not evidence or not isinstance(evidence, list) or not isinstance(evidence[0], str):
        return None
    h = re.sub(r"(?i)copyright|\(c\)|©|all rights reserved\.?|[0-9]{4}(?:\s*[-\u2013,]\s*[0-9]{4})*", " ", evidence[0])
    h = re.sub(r"^[\s*#/;!,.-]+|[\s*,.-]+$", "", h)
    return re.sub(r"\s+", " ", h).strip() or None


def write_markdown(summary, items, path):
    kinds = ["fail", "candidate"]
    lines = [f"# Release candidate check: {summary['rc']}", "",
             "Deterministic checks only. `fail` items are facts. `candidate` items need a person;",
             "most will be fine and some will not. Nothing here is a vote.", ""]
    lines.append("## Artifacts")
    for a in summary["artifacts"]:
        lines.append(f"- {a}")
    lines.append("")
    lines.append("## Counts")
    for k, v in summary["stats"].items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    for kind in kinds:
        chosen = [i for i in items if i["kind"] == kind]
        lines.append(f"## {kind} ({len(chosen)})")
        by_check = {}
        for i in chosen:
            by_check.setdefault((i["check"], i["message"]), []).append(i)
        for (check, msg), group in sorted(by_check.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"### {check}: {msg} ({len(group)})")
            if check.startswith("header-"):
                by_holder = {}
                for i in group:
                    h = holder(i["evidence"])
                    if h:
                        by_holder[h] = by_holder.get(h, 0) + 1
                if by_holder:
                    lines.append("By copyright holder: " + "; ".join(
                        f"{h} ({n})" for h, n in sorted(by_holder.items(), key=lambda kv: -kv[1])[:10]))
            for i in group[:EXAMPLES]:
                ev = i["evidence"]
                ev_s = ""
                if ev:
                    ev_s = json.dumps(ev) if not isinstance(ev, str) else ev
                    ev_s = " | " + ev_s[:300]
                lines.append(f"- `{i['path']}`{ev_s}")
            if len(group) > EXAMPLES:
                lines.append(f"- ... {len(group) - EXAMPLES} more in findings.json")
        lines.append("")
    media = [i for i in items if i["kind"] == "media"]
    if media:
        lines.append(f"## Images, fonts and documents ({len(media)})")
        lines.append("Usually fine. Fonts and icon sets are the ones that tend to carry their own licence.")
        for i in media[:EXAMPLES]:
            lines.append(f"- `{i['path']}`")
        if len(media) > EXAMPLES:
            lines.append(f"- ... {len(media) - EXAMPLES} more in findings.json")
        lines.append("")
    data = [i for i in items if i["kind"] == "data"]
    if data:
        lines.append(f"## Documents and data files ({len(data)})")
        lines.append("Usually test data. Worth a look if any is large or unexplained.")
        for i in data[:EXAMPLES]:
            lines.append(f"- `{i['path']}`")
        if len(data) > EXAMPLES:
            lines.append(f"- ... {len(data) - EXAMPLES} more in findings.json")
        lines.append("")
    nh = [i for i in items if i["kind"] == "no-header"]
    lines.append(f"## Code or documentation files with no licence header ({len(nh)})")
    for i in nh[:EXAMPLES]:
        lines.append(f"- `{i['path']}`")
    if len(nh) > EXAMPLES:
        lines.append(f"- ... {len(nh) - EXAMPLES} more in findings.json")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="dist/dev directory of the release candidate")
    src.add_argument("--rc-dir", help="local directory with the downloaded artifacts")
    ap.add_argument("--podling", help="podling slug; used to fetch KEYS if --keys is not given")
    ap.add_argument("--keys", help="KEYS file (path or URL)")
    ap.add_argument("--tag-dir", help="git checkout at the release tag, to compare with the source archive")
    ap.add_argument("--year", type=int, default=datetime.date.today().year, help="year the RC was cut")
    ap.add_argument("--disclaimer-template", help="standard disclaimer text from the Incubator policy, placeholders as {}")
    ap.add_argument("--wip-template", help="work-in-progress disclaimer text from the Incubator policy, placeholders as {}")
    ap.add_argument("--out", required=True, help="working directory for downloads, extraction and reports")
    args = ap.parse_args(argv)

    os.makedirs(args.out, exist_ok=True)
    f = Findings()
    stats = {"files": 0, "asf_header": 0, "no_header": 0, "spdx": 0, "third_party_header": 0,
             "asf_plus_foreign": 0, "binary": 0, "nested_archive": 0, "media": 0, "data": 0, "licence_signal": 0}

    if args.url:
        rc_dir = os.path.join(args.out, "artifacts")
        try:
            fetched = fetch_rc(args.url, rc_dir)
        except Exception as e:  # noqa: BLE001
            print(f"could not download the release candidate from {args.url}: {e}", file=sys.stderr)
            return 2
        if not fetched:
            print(f"no files listed at {args.url}", file=sys.stderr)
            return 2
        rc_label = args.url.rstrip("/").rsplit("/", 1)[-1]
    else:
        rc_dir = args.rc_dir
        rc_label = os.path.basename(os.path.abspath(rc_dir))

    keys_path = find_keys(args, rc_dir, f)
    home = gpg_home(keys_path) if keys_path else None

    templates = {}
    for kind, path in (("standard", args.disclaimer_template), ("wip", args.wip_template)):
        if path:
            with open(path, encoding="utf-8") as fh:
                templates[kind] = fh.read()

    # Everything signed or checksummed is a release artifact and gets the
    # naming, checksum and signature checks. Only archives are opened.
    listed = set(os.listdir(rc_dir))
    signed = {n[:-len(suf)] for n in listed for suf in (".asc",) + CHECKSUM_SUFFIXES + WEAK_CHECKSUM_SUFFIXES
              if n.endswith(suf)}
    artifacts = sorted(n for n in listed if is_archive(n) or (n in signed and n != "KEYS"))
    if not artifacts:
        f.fail("artifacts", "no release archives found", path=rc_dir)
    for n in artifacts:
        if not is_archive(n):
            f.info("artifacts", "not an archive; checked for naming, checksum and signature only", path=n)
        if "incubating" not in n:
            f.fail("naming", 'archive name does not contain "incubating"', path=n)
        else:
            f.ok("naming", 'archive name contains "incubating"', path=n)
        check_checksum(os.path.join(rc_dir, n), f)
        check_signature(os.path.join(rc_dir, n), home, f)
    # Which archive is the source release only matters for the tag comparison.
    # "-src", ".src" and "-source" are conventions, not policy, so when no
    # name matches every archive is compared with the tag.
    src = [n for n in artifacts if SOURCE_NAME.search(n)]
    if artifacts and not src:
        src = [n for n in artifacts if is_archive(n)]
        f.info("artifacts", "no archive name marks the source release; every archive is compared with the tag")

    for n in artifacts:
        if not is_archive(n):
            continue
        dest = os.path.join(args.out, "extracted", re.sub(r"(\.tar)?\.\w+$", "", n))
        try:
            safe_extract(os.path.join(rc_dir, n), dest)
        except Exception as e:  # noqa: BLE001
            f.fail("extract", "could not extract archive", path=n, evidence=str(e))
            continue
        root, top = top_dir(dest)
        if top is None:
            f.candidate("layout", "archive does not unpack into a single top-level directory", path=n)
        label = n
        check_root_files(root, label, args.year, f, templates)
        scan_tree(root, label, f, stats)
        if args.tag_dir and n in src:
            compare_with_tag(root, args.tag_dir, label, f)

    if home:
        shutil.rmtree(home, ignore_errors=True)

    summary = {"rc": rc_label, "artifacts": artifacts, "stats": stats,
               "counts": {k: sum(1 for i in f.items if i["kind"] == k)
                          for k in ("fail", "candidate", "ok", "info")}}
    with open(os.path.join(args.out, "findings.json"), "w", encoding="utf-8") as fh:
        json.dump({"summary": summary, "items": f.items}, fh, indent=1)
    write_markdown(summary, f.items, os.path.join(args.out, "findings.md"))
    print(json.dumps(summary, indent=1))
    return 1 if summary["counts"]["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
