#!/usr/bin/env python3
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Check internal links in the baked site.

Reads the HTML under one section of the baked output and checks that every
link to another page on incubator.apache.org resolves to a file in that
output. Works offline against the files, so it runs before anything is
published.

Relative links are the usual cause of breakage: a page in a subdirectory
that links to 'resources.html' points into its own directory, not the
section root.

Content that is copied in at publish time rather than baked (clutch,
projects, ip-clearance and the reserve data files) is not in the output, so
links into it are skipped.

Usage:
    python3 check_links.py SITE_DIR [--section training]

Exit codes:
    0  no broken links
    1  broken links found
    2  bad arguments
"""

import argparse
import os
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urldefrag, urljoin, urlparse

HOST = "incubator.apache.org"
BASE = "https://" + HOST + "/"

# Added to the published site from the asf-site reserve folder, not baked.
NOT_BAKED = ("clutch/", "projects/", "ip-clearance/")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.links.append((self.getpos()[0], value.strip()))


def target_exists(site_dir, path):
    if any(path.startswith(p) for p in NOT_BAKED):
        return True
    if "/" not in path and path.endswith((".txt", ".json")):
        return True
    full = os.path.join(site_dir, path)
    if path == "" or path.endswith("/"):
        return os.path.isfile(os.path.join(full, "index.html"))
    return os.path.isfile(full) or os.path.isfile(os.path.join(full, "index.html"))


def check(site_dir, section):
    broken = []
    root = os.path.join(site_dir, section)
    for dirpath, _, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith(".html"):
                continue
            page = os.path.join(dirpath, name)
            rel = os.path.relpath(page, site_dir).replace(os.sep, "/")
            parser = LinkParser()
            with open(page, encoding="utf-8", errors="replace") as f:
                parser.feed(f.read())
            for line, link in parser.links:
                if link.startswith(("#", "mailto:", "javascript:", "data:")):
                    continue
                url, _ = urldefrag(urljoin(BASE + rel, link))
                parsed = urlparse(url)
                if parsed.netloc != HOST:
                    continue
                path = unquote(parsed.path).lstrip("/")
                if not target_exists(site_dir, path):
                    broken.append((rel, line, link))
    return broken


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("site_dir", help="baked site output directory")
    ap.add_argument("--section", default="training",
                    help="subdirectory whose pages are checked (default: training)")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(args.site_dir, args.section)):
        print(f"no such directory: {os.path.join(args.site_dir, args.section)}",
              file=sys.stderr)
        return 2

    broken = check(args.site_dir, args.section)
    for page, line, link in broken:
        print(f"{page}:{line}: broken link {link}")
    if broken:
        print(f"{len(broken)} broken internal link(s)", file=sys.stderr)
        return 1
    print(f"no broken internal links under /{args.section}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
