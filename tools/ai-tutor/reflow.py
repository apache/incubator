#!/usr/bin/env python3
"""Rewrap prose in the lesson files to 80 columns.

Preserves structure: fenced code, headings, tables, indented blocks, blank
lines, and the bullet/number/blockquote markers with their hanging indents.
Only whitespace is allowed to change; the script verifies that itself.
"""
import re
import sys
import textwrap

WIDTH = 80

FENCE = re.compile(r'^\s*```')
HEADING = re.compile(r'^\s*#')
TABLE = re.compile(r'^\s*\|')
HRULE = re.compile(r'^\s*(-{3,}|\*{3,}|_{3,})\s*$')
HTML = re.compile(r'^\s*<')
QUOTE = re.compile(r'^\s*>')
INDENTED = re.compile(r'^ {4,}\S')
# "- foo", "* foo", "1. foo", "> - foo", "> 1. foo", "> foo"
# A list marker is at most three digits. Longer runs are prose, most often a
# year or a section number that happens to land at the start of a line.
MARKER = re.compile(r'^(?P<lead>\s*(?:>\s?)*)(?P<mark>(?:[-*+]\s+|\d{1,3}\.\s+)?)(?P<rest>\S.*)$')


def is_structural(line):
    return (
        not line.strip()
        or HEADING.match(line)
        or TABLE.match(line)
        or HRULE.match(line)
        or HTML.match(line)
        or QUOTE.match(line)
    )


def block_key(line):
    """Identity of the block a line belongs to: its lead (quote/indent) prefix."""
    m = MARKER.match(line)
    if not m:
        return None
    return m.group('lead')


def flush(buf, out):
    if not buf:
        return
    first = buf[0]
    m = MARKER.match(first)
    lead = m.group('lead')
    mark = m.group('mark')
    text = ' '.join(
        MARKER.match(l).group('rest') if MARKER.match(l) else l.strip()
        for l in buf
    )
    text = re.sub(r'\s+', ' ', text).strip()
    initial = lead + mark
    subsequent = lead + (' ' * len(mark))
    wrapped = textwrap.wrap(
        text,
        width=WIDTH,
        initial_indent=initial,
        subsequent_indent=subsequent,
        break_long_words=False,
        break_on_hyphens=False,
    )
    out.extend(wrapped or [initial.rstrip()])
    buf.clear()


def reflow(src):
    lines = src.split('\n')
    out = []
    buf = []
    in_fence = False
    start = 0
    # YAML frontmatter is structure, not prose. Pass it through untouched:
    # rewrapping it merges the keys onto one line and breaks the document.
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() in ('---', '...'):
                out.extend(lines[:i + 1])
                start = i + 1
                break
    for line in lines[start:]:
        if FENCE.match(line):
            flush(buf, out)
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if is_structural(line) or INDENTED.match(line):
            flush(buf, out)
            out.append(line)
            continue
        m = MARKER.match(line)
        if not m:
            flush(buf, out)
            out.append(line)
            continue
        # A bullet or number marker always starts a new block. Otherwise the
        # line continues the current one, whatever its indentation, because a
        # continuation line carries the hanging indent of its marker.
        if buf and m.group('mark'):
            flush(buf, out)
        buf.append(line)
    flush(buf, out)
    return '\n'.join(out)


def words(s):
    return re.sub(r'\s+', ' ', s).strip()


def main(paths):
    for p in paths:
        src = open(p).read()
        new = reflow(src)
        if words(src) != words(new):
            print(f'REFUSED {p}: content would change', file=sys.stderr)
            a, b = words(src), words(new)
            for i, (x, y) in enumerate(zip(a, b)):
                if x != y:
                    print('  at', i, repr(a[i - 60:i + 60]), file=sys.stderr)
                    print('  ->', repr(b[i - 60:i + 60]), file=sys.stderr)
                    break
            continue
        open(p, 'w').write(new)
        over = sum(1 for l in new.split('\n') if len(l) > WIDTH)
        print(f'{p}: ok, {over} lines still over {WIDTH}')


if __name__ == '__main__':
    main(sys.argv[1:])
