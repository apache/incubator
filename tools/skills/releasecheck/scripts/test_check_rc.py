#!/usr/bin/env python3
"""Regression test for check_rc.py.

Builds a fake release candidate with known problems, serves it over a local
HTTP server, runs check_rc.py against the URL, and checks every planted
problem is reported and nothing clean is flagged. Needs gpg on the path.

Run: python3 test_check_rc.py
"""

import functools
import gzip
import hashlib
import http.server
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import threading
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check_rc  # noqa: E402

ASF = ("/*\n * Licensed to the Apache Software Foundation (ASF) under one\n"
       " * or more contributor license agreements.\n */\n")
with open(os.path.join(HERE, "..", "references", "apache-license-2.0.txt"), encoding="utf-8") as _fh:
    AL2 = _fh.read()
# The alteration Seata 2.7.0 shipped: one word changed deep inside the licence text.
AL2_ALTERED = AL2.replace('"control" means (i) the power', '"control" means (properties) the power')
assert AL2_ALTERED != AL2


# Test data: the standard and WIP disclaimers as the Incubator policy words
# them, with the underlined phrases as {} placeholders.
STANDARD = ("Apache {} is an effort undergoing incubation at The Apache Software Foundation (ASF), "
            "sponsored by the {}. Incubation is required of all newly accepted projects until a further "
            "review indicates that the infrastructure, communications, and decision making process have "
            "stabilized in a manner consistent with other successful ASF projects. While incubation status "
            "is not necessarily a reflection of the completeness or stability of the code, it does indicate "
            "that the project has yet to be fully endorsed by the ASF.")
WIP = (STANDARD + " Some of the incubating project\u2019s releases may not be fully compliant with ASF policy. "
       "For example, releases may have incomplete or un-reviewed licensing conditions. What follows is a "
       "list of issues the project is currently aware of (this list is likely to be incomplete): {} "
       "If you are planning to incorporate this work into your product/project, please be aware that you "
       "will need to conduct a thorough licensing review to determine the overall implications of "
       "including this work. For the current status of this project through the Apache Incubator, visit: "
       "https://incubator.apache.org/projects/{}.html")
GOOD = STANDARD.replace("{}", "Demo", 1).replace("{}", "Apache Incubator", 1).replace("decision making", "decision-making")


EXPIRED_STATUS = (
    "[GNUPG:] KEYEXPIRED 1764769468\n"
    "[GNUPG:] EXPKEYSIG 71751399FB39CB84 Someone <someone@example.org>\n"
    "[GNUPG:] VALIDSIG 16D7A0B27D5ADD52BD57932971751399FB39CB84 2025-02-26 1740564372 0 4 0 1 8 00 16D7\n"
)


def disclaimer_unit_tests():
    """Direct checks on the comparison, independent of the fixture."""
    wip_ok = WIP.replace("{}", "Demo", 1).replace("{}", "Apache Incubator", 1)
    wip_ok = wip_ok.replace("{}", "- Bundled fonts not yet reviewed.", 1).replace("{}", "demo", 1)
    wip_empty = wip_ok.replace("- Bundled fonts not yet reviewed.", "List of known issues goes here")
    cases = [
        ("standard text matches", check_rc.compare_disclaimer(GOOD, STANDARD) == []),
        ("missing sentence caught", bool(check_rc.compare_disclaimer(GOOD.split(" While")[0], STANDARD))),
        ("custom wording caught", bool(check_rc.compare_disclaimer("Demo is incubating at the ASF.", STANDARD))),
        ("WIP text matches", check_rc.compare_disclaimer(wip_ok, WIP) == []),
        ("non-WIP text in WIP file caught", bool(check_rc.compare_disclaimer("0.7.1 is not an ASF release.", WIP))),
        ("WIP issues found", "fonts" in (check_rc.wip_issue_list(wip_ok) or "")),
        ("WIP placeholder seen", check_rc.wip_issue_list(wip_empty) == "list of known issues goes here"),
        ("-src name is a source release", bool(check_rc.SOURCE_NAME.search("apache-demo-1.0-incubating-src.tar.gz"))),
        (".src name is a source release", bool(check_rc.SOURCE_NAME.search("apache-xtable-0.4.0-incubating.src.tgz"))),
        ("-source-release name is a source release", bool(check_rc.SOURCE_NAME.search("demo-parent-2.1.0-incubating-source-release.zip"))),
        ("-bin name is not a source release", not check_rc.SOURCE_NAME.search("apache-demo-1.0-incubating-bin.tar.gz")),
        ("canonical AL2 text matches itself", check_rc.compare_al2(AL2) == []),
        ("altered AL2 text caught", bool(check_rc.compare_al2(AL2_ALTERED))),
        # gpg reports expiry against now, so the signature timestamp is what
        # says whether the key was still valid when the release was signed.
        ("signature timestamp and key expiry read",
         check_rc.sig_and_expiry(EXPIRED_STATUS) == (1740564372, 1764769468)),
        ("signed before expiry is not a failure",
         check_rc.sig_and_expiry(EXPIRED_STATUS)[0] < check_rc.sig_and_expiry(EXPIRED_STATUS)[1]),
        ("signed after expiry is still caught",
         check_rc.sig_and_expiry(EXPIRED_STATUS.replace("1740564372", "1790000000"))[0] > 1764769468),
        ("missing timestamps give no verdict",
         check_rc.sig_and_expiry("[GNUPG:] EXPKEYSIG ABC uid") == (None, None)),
        ("whole file type excluded is broad",
         check_rc.broad_excludes(["**/*.md", "src/**/*.py", "*.java"]) == ["**/*.md", "src/**/*.py", "*.java"]),
        ("data and build exclusions are not broad",
         check_rc.broad_excludes(["**/*.json", "**/*.lock", "target/**", "docs/*.md", "a/b.go"]) == []),
        ("excluding the whole tree is broad",
         check_rc.broad_excludes(["**"]) == ["**"]),
    ]
    for name, ok in cases:
        if not ok:
            print("  UNIT FAIL", name)
    return all(ok for _, ok in cases), len(cases)


def w(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data if isinstance(data, bytes) else data.encode())


def build(tmp):
    s = os.path.join(tmp, "src", "apache-demo-1.0.0-incubating-src")
    # The last line is a worked example, not a path: nothing named
    # "licenses/LICENSE-" is meant to exist, so it must not be reported.
    w(f"{s}/LICENSE", AL2_ALTERED + "\nThis product bundles leftpad (MIT). See licenses/LICENSE-leftpad.txt\n"
                          "This product bundles mitlib (MIT). See licenses/LICENSE-mitlib.txt\n"
                          "The text of each license is also in licenses/LICENSE-[project].txt\n"
                          # A real path under a hyphenated directory. Reading
                          # "ui-licenses/x" as "licenses/x" invents a missing file.
                          "This product bundles vben (MIT). See "
                          "dist-material/licenses/ui-licenses/license-vben.txt\n")
    w(f"{s}/dist-material/licenses/ui-licenses/license-vben.txt", "MIT\n")
    w(f"{s}/licenses/LICENSE-unused.txt", "MIT stub\n")
    w(f"{s}/licenses/LICENSE-mitlib.txt", "Copyright (c) 2014 Someone\nPermission is hereby granted\n")
    w(f"{s}/test/data.xlsx", b"PK\x03\x04\x00\x00xlsx")
    w(f"{s}/NOTICE", "Apache Demo (Incubating)\nCopyright 2024 The Apache Software Foundation\n\n"
                     "leftpad: Permission is hereby granted, free of charge\n")
    w(f"{s}/DISCLAIMER", "Apache Demo is an effort undergoing incubation at the ASF.\n")
    # Not an incubation disclaimer, and must not be judged as one.
    w(f"{s}/DISCLAIMER-BINARIES.txt",
      "The following binaries are included for testing only:\n- test/fixtures.zip\n")
    w(f"{tmp}/standard.txt", STANDARD)
    w(f"{tmp}/wip.txt", WIP)
    w(f"{s}/core/Good.java", ASF + "class Good {}\n")
    w(f"{s}/core/Copied.java", ASF + "/* Copyright 2019 Some Other Corp. */\nclass Copied {}\n")
    w(f"{s}/core/NoYear.go", ASF.replace("/*", "//").replace(" */", "") + "// Copyright The Kubernetes Authors.\npackage x\n")
    w(f"{s}/core/spdx_mit.js", "// SPDX-License-Identifier: MIT\nx=1\n")
    w(f"{s}/core/spdx_al2.js", "// SPDX-License-Identifier: Apache-2.0\ny=1\n")
    w(f"{s}/core/noheader.js", "z=1\n")
    w(f"{s}/core/gpl.c", "/* under the terms of the GNU General Public License v3 */\nint main(){}\n")
    w(f"{s}/vendor/leftpad/index.js", "/*! leftpad (c) 2014 Someone | MIT */\nm=1\n")
    w(f"{s}/site/thirdparty.html", "Copyright 2015 Google Inc.\nLicensed under the Apache License, Version 2.0\n")
    w(f"{s}/site/logo.png", b"\x89PNG\r\n\x1a\n\x00\x00")
    w(f"{s}/site/banner.css", ASF + "/*! normalize.css v2.1.3 | MIT License | git.io/normalize */\nhtml{}\n")
    w(f"{s}/core/ported.rs", ASF + "// This implementation is derived from the `oneshot` crate.\nfn x() {}\n")
    w(f"{s}/README.md", "Build with ./mvnw -pl utilities package\n")
    w(f"{s}/docs/guide.md", "# Guide\n\nSome documentation without a header.\n")
    w(f"{s}/gradle/wrapper/gradle-wrapper.jar", b"PK\x03\x04\x00\x00bin")
    # A jar of classes is compiled code. A jar with none is a test fixture,
    # and calling it compiled code is how a reviewer gets sent down a hole.
    jb = io.BytesIO()
    with zipfile.ZipFile(jb, "w") as z:
        z.writestr("META-INF/MANIFEST.MF", b"Manifest-Version: 1.0\n")
    w(f"{s}/test/empty.jar", jb.getvalue())
    jb = io.BytesIO()
    with zipfile.ZipFile(jb, "w") as z:
        z.writestr("org/demo/Compiled.class", b"\xca\xfe\xba\xbe\x00\x00")
    w(f"{s}/test/classes.jar", jb.getvalue())
    w(f"{s}/src/bin/MSG00001.bin", "MessageId=1\nLanguage=English\n")
    w(f"{s}/.DS_Store", b"\x00\x00")
    # macOS resource forks, including one beside the top-level directory, which
    # must not stop the real root being found.
    w(f"{s}/._pom.xml", b"\x00\x05\x16\x07AppleDouble")
    w(f"{s}/core/._Good.java", b"\x00\x05\x16\x07AppleDouble")
    tw = io.BytesIO()
    with tarfile.open(fileobj=tw, mode="w:gz") as t:
        d = b"tweet\n"
        i = tarfile.TarInfo("tweets.txt")
        i.size = len(d)
        t.addfile(i, io.BytesIO(d))
    w(f"{s}/test/tweets.tar.gz", tw.getvalue())
    w(f"{s}/test/data.csv.gz", gzip.compress(b"a,b\n1,2\n"))
    w(f"{s}/test/tool.gz", gzip.compress(b"\x7fELF\x02\x01\x01\x00" + b"\x00" * 64))
    zb = io.BytesIO()
    with zipfile.ZipFile(zb, "w") as z:
        z.writestr("Evil.class", b"\xca\xfe\xba\xbe\x00\x00")
    w(f"{s}/test/fixtures.zip", zb.getvalue())

    # The project's own licence-audit configuration. A header count reported
    # without this produces false blockers, so both places are planted.
    # The last two sweep whole file types the header policy covers, which is
    # how a project makes RAT pass without anyone looking at those files.
    w(f"{s}/.rat-excludes",
      "# generated\nsrc/generated/**\ntestdata/*.golden\n**/*.json\n**/*.md\n**/*.js\n")
    w(f"{s}/pom.xml",
      '<project xmlns="http://maven.apache.org/POM/4.0.0"><build><plugins><plugin>\n'
      "<groupId>org.apache.rat</groupId><artifactId>apache-rat-plugin</artifactId>\n"
      "<configuration><excludes>\n"
      "<exclude>options/flag.go</exclude>\n<exclude>options/options.go</exclude>\n"
      "<exclude>end_to_end/resources/**</exclude>\n"
      "</excludes></configuration></plugin></plugins></build></project>\n")
    # A git submodule the tag checkout never fetched. Every file under it is in
    # the archive only, and none of them is a file the release added.
    w(f"{s}/gsub/bench/bench.h", "// upstream benchmark header\n")
    w(f"{s}/gsub/bench/README.md", "# google benchmark\n")

    tag = os.path.join(tmp, "tag")
    shutil.copytree(s, tag)
    os.remove(f"{tag}/.DS_Store")
    shutil.rmtree(f"{tag}/gsub/bench")
    os.makedirs(f"{tag}/gsub/bench")
    w(f"{tag}/.gitmodules", '[submodule "gsub/bench"]\n\tpath = gsub/bench\n'
                            "\turl = https://github.com/google/benchmark.git\n")
    w(f"{tag}/utilities/Tool.java", ASF + "class Tool {}\n")  # in the tag, not in the archive, named in README
    with open(f"{tag}/core/Good.java", "a") as f:
        f.write("// changed\n")

    rc = os.path.join(tmp, "www", "rc1")
    os.makedirs(rc)
    ad = os.path.join(tmp, "_ad")
    w(ad, b"\x00\x05\x16\x07AppleDouble")
    with tarfile.open(f"{rc}/apache-demo-1.0.0-incubating-src.tar.gz", "w:gz") as t:
        t.add(s, arcname="apache-demo-1.0.0-incubating-src")
        t.add(ad, arcname="._apache-demo-1.0.0-incubating-src")
    b = os.path.join(tmp, "bin", "apache-demo-1.0.0-bin")
    w(f"{b}/LICENSE", AL2)
    w(f"{b}/NOTICE", "Apache Demo\nCopyright 2026 The Apache Software Foundation\n")
    shutil.make_archive(f"{rc}/apache-demo-1.0.0-bin", "zip", os.path.dirname(b), "apache-demo-1.0.0-bin")

    home = os.path.join(tmp, "gnupg")
    os.makedirs(home, mode=0o700)
    g = ["gpg", "--homedir", home, "--batch", "--quiet", "--passphrase", ""]
    subprocess.run(g + ["--quick-gen-key", "RM <rm@apache.org>", "ed25519", "sign", "never"], check=True)
    subprocess.run(g + ["--quick-gen-key", "X <x@example.com>", "ed25519", "sign", "never"], check=True)
    with open(os.path.join(tmp, "www", "KEYS"), "wb") as f:
        f.write(subprocess.run(["gpg", "--homedir", home, "--armor", "--export", "rm@apache.org"],
                               capture_output=True, check=True).stdout)
    src = f"{rc}/apache-demo-1.0.0-incubating-src.tar.gz"
    zipf = f"{rc}/apache-demo-1.0.0-bin.zip"
    subprocess.run(g + ["--local-user", "rm@apache.org", "--armor", "--detach-sign", src], check=True)
    subprocess.run(g + ["--local-user", "x@example.com", "--armor", "--detach-sign", zipf], check=True)
    with open(src, "rb") as f:
        w(src + ".sha512", hashlib.sha512(f.read()).hexdigest() + "  " + os.path.basename(src) + "\n")
    w(zipf + ".sha512", "0000  apache-demo-1.0.0-bin.zip\n")
    # A signed wheel: not opened, but its name still needs "incubating".
    whl = f"{rc}/apache_demo-1.0.0-py3-none-any.whl"
    w(whl, b"PK\x03\x04wheel")
    subprocess.run(g + ["--local-user", "rm@apache.org", "--armor", "--detach-sign", whl], check=True)
    with open(whl, "rb") as f:
        w(whl + ".sha512", hashlib.sha512(f.read()).hexdigest() + "\n")
    w(zipf + ".md5", "0000\n")
    return tag


EXPECT = [
    ("naming", "bin.zip", "fail"), ("checksum", "bin.zip", "fail"), ("signature", "bin.zip", "fail"),
    ("disclaimer", "bin.zip", "fail"), ("license", "LICENSE", "fail"),
    ("checksum", "incubating-src.tar.gz", "ok"), ("signature", "incubating-src.tar.gz", "ok"),
    ("notice", "NOTICE", "candidate"), ("header-provenance", "Copied.java", "candidate"),
    ("header-provenance", "NoYear.go", "candidate"), ("data", "data.xlsx", None),
    ("header-third-party", "leftpad/index.js", "candidate"), ("header-third-party", "thirdparty.html", "candidate"),
    ("header-other-licence", "spdx_mit.js", "candidate"), ("header-spdx-only", "spdx_al2.js", "candidate"),
    ("licence-signal", "gpl.c", "candidate"), ("binary", "gradle-wrapper.jar", "fail"),
    ("binary", "fixtures.zip", "candidate"), ("binary", "tool.gz", "candidate"),
    ("nested-archive", "tweets.tar.gz", "candidate"), ("nested-archive", "data.csv.gz", "candidate"),
    ("vendored", "vendor", "candidate"), ("junk", ".DS_Store", "candidate"),
    ("license", "LICENSE-unused.txt", "candidate"), ("vs-tag", "Good.java", "candidate"),
    ("checksum", "bin.zip", "candidate"), ("media", "logo.png", None), ("no-header", "noheader.js", None),
    ("naming", "any.whl", "fail"), ("signature", "any.whl", "ok"), ("checksum", "any.whl", "ok"),
    ("disclaimer", "incubating-src.tar.gz/DISCLAIMER", "candidate"),
    ("license-text", "incubating-src.tar.gz/LICENSE", "fail"), ("license-text", "bin.zip/LICENSE", "ok"),
    ("header-provenance", "banner.css", "candidate"), ("provenance-note", "ported.rs", "candidate"),
    ("vs-tag", "incubating-src.tar.gz/utilities", "candidate"),
    ("no-header", "guide.md", None),
    ("junk", "incubating-src.tar.gz", "candidate"),
    ("no-header", "incubating-src.tar.gz", "info"),
    ("vs-tag", "incubating-src.tar.gz", "info"),
    ("nested-archive", "empty.jar", "candidate"), ("binary", "classes.jar", "candidate"),
    ("no-header", "incubating-src.tar.gz", "candidate"),
]


def main():
    tmp = tempfile.mkdtemp(prefix="check-rc-test-")
    try:
        tag = build(tmp)
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *a):
                pass

        handler = functools.partial(Quiet, directory=os.path.join(tmp, "www"))
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        out = os.path.join(tmp, "out")
        rc = check_rc.main(["--url", f"{base}/rc1/", "--keys", f"{base}/KEYS", "--tag-dir", tag,
                            "--year", "2026", "--out", out,
                            "--disclaimer-template", os.path.join(tmp, "standard.txt"),
                            "--wip-template", os.path.join(tmp, "wip.txt")])
        srv.shutdown()
        with open(os.path.join(out, "findings.json")) as f:
            items = json.load(f)["items"]

        def has(check, part, kind):
            return any(i["check"] == check and part in (i["path"] or "") and (kind is None or i["kind"] == kind)
                       for i in items)

        missing = [e for e in EXPECT if not has(*e)]
        false_pos = [i for i in items
                     if ("MSG00001" in (i["path"] or "") and i["check"] == "binary")
                     or (i["check"] == "license" and "LICENSE-2.0" in json.dumps(i["evidence"]))
                     or ("LICENSE-mitlib" in (i["path"] or "") and i["check"].startswith("header"))
                     or ("data.xlsx" in (i["path"] or "") and i["check"] == "binary")
                     or ("Good.java" in (i["path"] or "") and i["check"].startswith("header"))
                     or ("bin.zip/LICENSE" in (i["path"] or "") and i["check"] == "license-text" and i["kind"] == "fail")
                     or ("README.md" in (i["path"] or "") and i["check"] in ("provenance-note", "no-header"))
                     or (i["check"] == "root-files" and i["kind"] == "fail"
                         and "incubating-src" in (i["path"] or ""))
                     or (i["check"] == "layout" and "incubating-src" in (i["path"] or ""))
                     or ("gsub/bench" in (i["path"] or "") and i["check"] == "vs-tag"
                         and i["kind"] == "candidate")
                     or ("empty.jar" in (i["path"] or "") and i["check"] == "binary")
                     or (i["check"] == "license" and i["kind"] == "fail"
                         and "LICENSE-[" in json.dumps(i["evidence"] or ""))
                     or (i["check"] == "license" and i["kind"] == "fail"
                         and json.dumps(i["evidence"] or "").rstrip('"').endswith("LICENSE-"))
                     or (i["check"] == "license" and "LICENSES/" in (i["path"] or ""))
                     or ("DISCLAIMER-BINARIES" in (i["path"] or "")
                         and i["kind"] in ("fail", "candidate"))
                     or (i["check"] == "license" and i["kind"] == "fail"
                         and "vben" in json.dumps(i["evidence"] or ""))
                     or (i["check"] in ("root-files", "disclaimer") and i["kind"] == "fail"
                         and "nested" in (i["path"] or ""))]
        units_ok, units = disclaimer_unit_tests()
        ok = rc == 1 and not missing and not false_pos and units_ok
        print(f"exit code {rc} (expected 1)")
        print(f"{len(EXPECT) - len(missing)}/{len(EXPECT)} planted problems found")
        print(f"disclaimer unit checks {'passed' if units_ok else 'FAILED'} ({units})")
        for m in missing:
            print("  MISSING", m)
        for fp in false_pos:
            print("  FALSE POSITIVE", fp["check"], fp["path"])
        print("PASS" if ok else "FAIL")
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
