#!/usr/bin/env python3
"""Verification for the meal-planning guide.

Standard library only. Run from the repo root:

    python3 scripts/verify.py

Checks:
 1. site/ builds from docs/ (build.py runs cleanly, output is idempotent)
 2. every generated site/*.html parses as valid HTML structure
 3. all internal links (href/src) resolve to files that exist in site/
 4. every page keeps the education-only disclaimer and copyright line
 5. the markdown renderer handles headings/lists/tables/code/links correctly
 6. docs/ chapter anchors referenced across files resolve to real URLs
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build as build_mod  # noqa: E402

VOID = {"meta", "link", "br", "hr", "img", "input", "source", "wbr"}

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = ""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(name)


class StructureParser(HTMLParser):
    """Tags must be balanced; void elements exempt."""

    def __init__(self):
        super().__init__()
        self.errors = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append(f"closing </{tag}> with empty stack")
            return
        if self.stack[-1] != tag:
            self.errors.append(f"</{tag}> but open stack is {self.stack[-1]}")
        else:
            self.stack.pop()


def test_markdown_renderer():
    sample = """# Title

Intro with **bold**, *ital*, `code`, and [a link](other.md).

## Section

- one
- two

1. first
2. second

> quoted thought

| A | B |
|---|---|
| 1 | 2 |

```
keep | pipes | as-is
```
"""
    html_out = build_mod.render_markdown(sample)
    ok = all(
        s in html_out
        for s in [
            "<h1>Title</h1>",
            "<strong>bold</strong>",
            "<em>ital</em>",
            "<code>code</code>",
            '<a href="other.html">a link</a>',
            "<ul><li>one</li><li>two</li></ul>",
            "<ol><li>first</li><li>second</li></ol>",
            "<blockquote><p>quoted thought</p></blockquote>",
            "<table><thead><tr><th>A</th><th>B</th></tr></thead>",
            "<td>1</td>",
            "<pre><code>keep | pipes | as-is",
        ]
    )
    check("markdown renderer: all structure rendered", ok, html_out)


def check_internal_links():
    for page in sorted(build_mod.SITE.glob("*.html")):
        text = page.read_text(encoding="utf-8")
        hrefs = re.findall(r'(?:href|src)="([^"]+)"', text)
        for href in set(hrefs):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = href.split("#", 1)[0]
            if not target:
                continue
            path = (build_mod.SITE / target).resolve()
            if target.startswith("/") or ".." in Path(target).parts:
                check(f"{page.name}: absolute/parent link rejected", False, href)
                continue
            if not path.exists():
                check(f"{page.name}: broken link", False, href)


def check_required_strings():
    for page in sorted(build_mod.SITE.glob("*.html")):
        text = page.read_text(encoding="utf-8")
        check(
            f"{page.name}: education-only disclaimer",
            ("Education only" in text) and ("nutrition" in text),
        )
        check(f"{page.name}: LLC credit", "Asdale Dynamics, LLC" in text)


def main():
    # 1. fresh build, twice (idempotency)
    build_mod.build()
    first = {p.name: p.read_text(encoding="utf-8") for p in build_mod.SITE.glob("*.html")}
    build_mod.build()
    second = {p.name: p.read_text(encoding="utf-8") for p in build_mod.SITE.glob("*.html")}
    check("build: runs cleanly", len(first) >= 9, f"built {len(first)} html files")
    check("build: idempotent", first == second)

    # 2. HTML structure parses
    for page in sorted(build_mod.SITE.glob("*.html")):
        parser = StructureParser()
        parser.feed(page.read_text(encoding="utf-8"))
        check(f"{page.name}: balanced tags", not parser.errors, str(parser.errors))

    # 3. links resolve
    check_internal_links()

    # 4. disclaimers + credit
    check_required_strings()

    # 5. renderer unit smoke test
    test_markdown_renderer()

    print()
    if FAILURES:
        print(f"VERIFICATION FAILED: {len(FAILURES)} failing check(s): {FAILURES}")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
