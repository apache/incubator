#!/usr/bin/env python3
"""Publish the lesson prompts as plain files for the website.

The lesson markdown files under tools/ai-tutor/ are the only copy of this
material in the repository. This script does not add a second one: it is run
during the site build and writes the prompt bodies straight into the baked
output, so the published files are produced from the source every time the site
is built and cannot drift from it.

What it strips is the preamble above the first horizontal rule, which is
addressed to whoever is deploying the lesson and is explicitly not part of the
prompt. What lands on the website is exactly the text a learner should paste.

Usage, from the repository root:
    python3 tools/ai-tutor/publish-lessons.py --out "$WORKDIR/training/lessons"
"""

import argparse
import glob
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_builder():
    """Reuse the parsing in build-skill.py rather than restating it here."""
    path = os.path.join(HERE, 'build-skill.py')
    spec = importlib.util.spec_from_file_location('build_skill', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def publish(source, out):
    builder = _load_builder()
    lessons = builder.scan(source)
    if not lessons:
        raise SystemExit(f'no lessons found in {source}')

    os.makedirs(out, exist_ok=True)
    for l in lessons:
        dest = os.path.join(out, f"lesson-{l['number']:02d}.md")
        body = l['body'] if l['body'].endswith('\n') else l['body'] + '\n'
        with open(dest, 'w') as fh:
            fh.write(body)
        # A learner pasting from the website must get the same tutor as one
        # pasting from the repository, so prove the copy rather than trust it.
        if open(dest).read().strip() != l['body'].strip():
            raise SystemExit(f"{dest}: does not match {l['source']}")
        print(f"  lesson-{l['number']:02d}.md  <- {l['source']}")

    print(f'published {len(lessons)} lesson prompts to {out}')
    return lessons


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', default=HERE,
                    help='directory holding the lesson-NN-*.md files')
    ap.add_argument('--out', required=True,
                    help='directory to write the published prompts into')
    args = ap.parse_args()
    publish(args.source, args.out)


if __name__ == '__main__':
    main()
