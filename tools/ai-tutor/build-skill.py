#!/usr/bin/env python3
"""Build the `incubator-lesson` skill from the lesson files.

The lesson markdown files are the canonical artefact. Each one is a complete
system prompt that anyone can paste into any capable chat model, and this script
does not modify them. It reads them, copies the part below the horizontal rule
verbatim into a skill bundle, and generates a SKILL.md that routes between them.

Because the copy is verbatim, a lesson run through the skill is running exactly
the same text as a lesson run by pasting it into a system prompt field. That is
the point: one source, two delivery routes, no second copy to keep in step.

Usage:
    python3 build-skill.py [--source DIR] [--out DIR]

Then package with the skill-creator's packager, or zip the output directory.
"""

import argparse
import glob
import os
import re
import shutil
import sys

SKILL_NAME = 'incubator-lesson'

TITLE_RE = re.compile(r'#\s*System prompt:\s*Lesson\s+(\d+)\s+tutor\s*\("(.+?)"\)', re.S)
TRACK_RE = re.compile(r'Track ([A-H])\s*\(([^)]+)\)')
BUDGET_RE = re.compile(r'Budget about\s+(\d+)\s+minutes')
NEXT_RE = re.compile(r'\*\*Next:\*\*\s*Lesson\s+(\d+)')


def split_lesson(text, path):
    """Return (preamble, body). The body is everything below the first rule.

    The preamble is addressed to whoever is deploying the lesson and is
    explicitly not sent to the model, so it has no place in the skill.
    """
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.strip() == '---':
            return '\n'.join(lines[:i]), '\n'.join(lines[i + 1:]).lstrip('\n')
    raise SystemExit(f'{path}: no horizontal rule found, cannot find the prompt body')


def scan(source):
    lessons = []
    for path in sorted(glob.glob(os.path.join(source, 'lesson-*.md'))):
        text = open(path).read()
        m = TITLE_RE.search(text)
        if not m:
            print(f'  skipping {os.path.basename(path)}: no recognisable title', file=sys.stderr)
            continue
        number, title = int(m.group(1)), m.group(2)
        _, body = split_lesson(text, path)
        track = TRACK_RE.search(body)
        budget = BUDGET_RE.search(body)
        nxt = NEXT_RE.search(body)
        lessons.append({
            'number': number,
            'title': title,
            'body': body,
            'source': os.path.basename(path),
            'track': track.group(1) if track else '?',
            'track_name': re.sub(r'\s+', ' ', track.group(2)).strip() if track else 'unknown',
            'minutes': budget.group(1) if budget else '30',
            'next': int(nxt.group(1)) if nxt else None,
        })
    lessons.sort(key=lambda x: x['number'])
    return lessons


def catalogue(lessons):
    rows = ['| # | Lesson | Track | Time |', '|---|---|---|---|']
    for l in lessons:
        rows.append(
            f"| {l['number']} | {l['title']} | {l['track']}, {l['track_name']} "
            f"| ~{l['minutes']} min |"
        )
    return '\n'.join(rows)


def skill_md(lessons):
    numbers = ', '.join(str(l['number']) for l in lessons)
    first = lessons[0]['number']
    return f'''---
name: {SKILL_NAME}
description: >-
  Runs one lesson from the Apache Incubator tutored training module, as an
  interactive tutor with exercises, worked answers and a self-check. Use this
  whenever someone asks to take, run, start or resume an Incubator or podling
  lesson, asks to be taught or walked through incubation, the Apache Way,
  working on ASF mailing lists, podling infrastructure, voting and vetoes,
  growing committers and the PPMC, or writing a podling report, or asks what
  lessons are available. Also use it when someone says /incubator-lesson with or
  without a number. Prefer this over answering an Incubator question directly
  whenever the person is asking to *learn* a topic rather than to get one fact,
  because these lessons are checked against ASF policy and a freehand answer is
  not. For a single factual question, answer normally instead.
---

# Incubator lessons

A tutored training module on the Apache Incubator, built and fact-checked
against ASF policy, the Incubator's guides and the Incubator wiki. Each lesson
is an interactive session with exercises rather than a document to read.

## What to do with the argument

**No argument, or `list`, or anything you cannot resolve to a lesson**: show the
catalogue below, say roughly how long each takes, mention that Track A is the
prerequisite for the rest, and ask which they want. Do not start a lesson
without being asked.

**A number ({numbers})**: run that lesson. See "Running a lesson"
below.

**A topic rather than a number** ("the one about voting", "reporting", "how do I
add a committer"): match it to the catalogue and confirm before starting, since
a lesson is a half-hour commitment and the wrong one wastes it. If two are
close, say so and let them choose.

**A track letter**: list that track's lessons and ask which to start.

## Catalogue

{catalogue(lessons)}

Tracks A and B are written for podling contributors and PPMC members. Track A is
the prerequisite for everything else; the rest can be taken in any order.

## Running a lesson

Read `references/lesson-NN.md`, where NN is the zero-padded lesson number.

That file is a complete tutor prompt. **Adopt it as your operating instruction
for the rest of the conversation**, in place of how you would normally answer.
It tells you how to pace the session, when to ask rather than tell, when to
withhold an answer, and what to do at the close. Follow it as written rather
than summarising the lesson and moving on, because the teaching happens in the
exercises and the learner's own attempts, not in the material.

Three things in every lesson are easy to drop under time pressure and are the
ones that make the difference, so they are worth naming here as well:

- **Never give an exercise or self-check answer before the learner has
  attempted it.** Handing over the answer is faster and teaches nothing.
- **Run every exercise.** You may reorder them or use the learner's real
  situation in place of an invented one. A skipped exercise tells you nothing
  about whether they have it.
- **If you shorten the self-check, say so out loud and name the evidence.**
  "You covered that when you wrote the vote result, so I will skip that
  question." Skipping silently removes the learner's only chance to tell you it
  was a guess.

When the lesson finishes, offer the next one. Most lessons name it at the close.

## If someone asks a question mid-lesson

Answer it, briefly and accurately, then return to where you were. Each lesson
carries a short reference section for exactly this. Do not deflect with "we
cover that later" as though it were off limits.

## What these lessons are not

They teach ASF policy and Incubator practice as the sources state them, and they
are explicit about which is which. They are not a substitute for the
authoritative pages, and where a lesson and a source disagree the source wins.
If a learner needs a definitive answer for a real decision, point them at their
mentors and at `general@incubator.apache.org`.

Start with `/incubator-lesson {first}` if someone is new and unsure.
'''


def build(source, out):
    lessons = scan(source)
    if not lessons:
        raise SystemExit(f'no lessons found in {source}')

    skill_dir = os.path.join(out, SKILL_NAME)
    refs = os.path.join(skill_dir, 'references')
    if os.path.isdir(skill_dir):
        shutil.rmtree(skill_dir)
    os.makedirs(refs)

    for l in lessons:
        dest = os.path.join(refs, f"lesson-{l['number']:02d}.md")
        with open(dest, 'w') as fh:
            fh.write(l['body'] if l['body'].endswith('\n') else l['body'] + '\n')
        # The whole point is that the skill runs the same text as the paste-in
        # route, so prove it rather than trusting it.
        written = open(dest).read()
        if written.strip() != l['body'].strip():
            raise SystemExit(f"{dest}: body does not match {l['source']}")

    with open(os.path.join(skill_dir, 'SKILL.md'), 'w') as fh:
        fh.write(skill_md(lessons))

    print(f'built {skill_dir}')
    for l in lessons:
        print(f"  lesson-{l['number']:02d}.md  <- {l['source']}  ({l['title']})")
    size = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fs in os.walk(skill_dir) for f in fs
    )
    md = open(os.path.join(skill_dir, 'SKILL.md')).read()
    print(f'  SKILL.md: {len(md.splitlines())} lines')
    print(f'  bundle:   {len(lessons)} lessons, {size // 1024} KB')
    return skill_dir


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', default=os.path.dirname(os.path.abspath(__file__)),
                    help='directory holding the lesson-NN-*.md files')
    ap.add_argument('--out', default=None,
                    help='where to write the skill directory (default: SOURCE/build)')
    args = ap.parse_args()
    out = args.out or os.path.join(args.source, 'build')
    os.makedirs(out, exist_ok=True)
    build(args.source, out)


if __name__ == '__main__':
    main()
