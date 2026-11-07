#!/usr/bin/env python3
"""Builds the static site in site/ from the markdown manual in docs/.

Standard library only, no external dependencies. Run from the repo root:

    python3 scripts/build.py
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

DOC_URLS = {
    "index.md": "index.html",
    "01-pantry-first-prompts.md": "01-pantry-first-prompts.html",
    "02-short-order-nights.md": "02-short-order-nights.html",
    "03-picky-eater-workarounds.md": "03-picky-eater-workarounds.html",
    "04-grocery-lists-you-can-edit.md": "04-grocery-lists-you-can-edit.html",
    "05-local-ai-with-ollama.md": "05-local-ai-with-ollama.html",
    "06-prompt-library.md": "06-prompt-library.html",
    "07-printable-planner.md": "07-printable-planner.html",
}

CHAPTER_ORDER = [d for d in DOC_URLS if d not in ("index.md",)]

DISCLAIMER = (
    "<strong>Education only — never nutrition or medical advice.</strong> "
    "For dietary and health decisions, talk to your doctor or a registered dietitian."
)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Meal Planning with Free AI</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <p class="kicker">Asdale Dynamics · Beginner AI Series</p>
    <h1><a href="index.html" style="color:inherit;text-decoration:none">{title}</a></h1>
    <p class="tagline">{subtitle}</p>
    <p class="disclaimer">{disclaimer}</p>
  </div>
</header>
<main class="wrap">
{body}
<nav class="chapter-nav" aria-label="Chapter navigation">
  {prev_link}<a href="index.html">Manual home</a>{next_link}
</nav>
</main>
<footer class="site-footer">
  <div class="wrap">
    <p>Part of the beginner AI series by Asdale Dynamics, LLC — plain-English AI guides, books, and tools. Companion manual: <em>The Massive AI Manual</em> by Dylan Asdale.</p>
    <p>© 2026 Asdale Dynamics, LLC · MIT licensed · Education only, never medical or nutrition advice.</p>
  </div>
</footer>
</body>
</html>
"""


def inline(text: str) -> str:
    """Render inline markdown (code, links, bold, italic) to HTML."""
    out = html.escape(text, quote=False)
    placeholders = []

    def stash(token: str) -> str:
        placeholders.append(token)
        return f"\x00{len(placeholders) - 1}\x00"

    out = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{m.group(1)}</code>"), out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: stash(f'<a href="{m.group(2)}">{m.group(1)}</a>'), out)
    out = re.sub(r"\*\*([^*]+)\*\*", lambda m: stash(f"<strong>{m.group(1)}</strong>"), out)
    out = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", lambda m: stash(f"<em>{m.group(1)}</em>"), out)
    out = re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], out)
    return out


def link_fix(url: str) -> str:
    """Rewrite docs-relative links to site-relative pages."""
    if url.startswith(("http://", "https://", "mailto:", "#")):
        return url
    url = url.replace("../site/", "")
    if url in DOC_URLS.values():
        return url
    if url.endswith(".md"):
        slug = url.rsplit("/", 1)[-1]
        return "index.html" if slug == "index.md" else slug[:-3] + ".html"
    return url


def render_markdown(md: str) -> str:
    """Minimal markdown-to-HTML: headings, paragraphs, lists, blockquotes,
    fenced code, GFM tables, hr. Sufficient for this manual's docs/."""
    blocks: list[str] = []
    lines = md.splitlines()
    i = 0
    list_re = re.compile(r"^\s*-\s+(.*)$")
    olist_re = re.compile(r"^\s*\d+\.\s+(.*)$")
    table_sep = re.compile(r"^\s*\|?[\s:-]*-{3}[\s:|:-]*\|?\s*$")

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("```"):
            code, end = [], i + 1
            while end < len(lines) and not lines[end].strip().startswith("```"):
                code.append(lines[end])
                end += 1
            blocks.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
            i = end + 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            blocks.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        stripped = line.strip()
        if stripped == "---":
            blocks.append("<hr>")
            i += 1
            continue

        if "|" in line and i + 1 < len(lines) and "|" in lines[i + 1] and table_sep.match(lines[i + 1]):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and "|" in lines[j] and lines[j].strip():
                rows.append([inline(c.strip()) for c in lines[j].strip().strip("|").split("|")])
                j += 1
            parts = ["<table><thead><tr>"]
            parts += [f"<th>{inline(c)}</th>" for c in header]
            parts.append("</tr></thead><tbody>")
            for row in rows:
                parts.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
            parts.append("</tbody></table>")
            blocks.append("".join(parts))
            i = j
            continue

        if stripped.startswith(">"):
            quote, j = [], i
            while j < len(lines) and lines[j].strip().startswith(">"):
                quote.append(lines[j].lstrip().lstrip(">").strip())
                j += 1
            blocks.append("<blockquote><p>" + inline(" ".join(q for q in quote if q)) + "</p></blockquote>")
            i = j
            continue

        m, kind = list_re.match(line), None
        if m:
            kind = "ul"
        else:
            m, kind = olist_re.match(line), "ol"
        if m:
            items = []
            match_re = list_re if kind == "ul" else olist_re
            while i < len(lines) and (mm := match_re.match(lines[i])):
                items.append(f"<li>{inline(mm.group(1))}</li>")
                i += 1
            blocks.append(f"<{kind}>" + "".join(items) + f"</{kind}>")
            continue

        if not stripped:
            i += 1
            continue

        para, j = [], i
        table_stop = re.compile(r"^(#{1,4}\s|[-]\s|\d+\.\s|>|\s*```|\||---\s*$)")
        while j < len(lines) and lines[j].strip() and not table_stop.match(lines[j]):
            para.append(lines[j].strip())
            j += 1
        if para:
            blocks.append("<p>" + inline(" ".join(para)) + "</p>")
            i = j
        else:
            blocks.append(f"<p>{inline(stripped)}</p>")
            i += 1

    # second pass: rewrite any .hrefs left plain inside code-stashed links
    out = "\n".join(blocks)
    out = re.sub(r'href="([^"]*)"', lambda m: f'href="{link_fix(m.group(1))}"', out)
    return out


def subtitle_for(md_after_title: str) -> str:
    """First non-heading line under the H1, italic taglines get unwrapped."""
    for line in md_after_title.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        clean = stripped.strip("*").strip()
        return inline(clean) if clean else ""
    return "Beginner manual"


def build():
    SITE.mkdir(exist_ok=True)
    for name in CHAPTER_ORDER:
        md = (DOCS / name).read_text(encoding="utf-8")
        title_match = re.match(r"^#\s+(.+)$", md.splitlines()[0])
        title = title_match.group(1) if title_match else name
        body = render_markdown(md)
        after = "\n".join(md.splitlines()[1:])
        subtitle = subtitle_for(after)
        idx = CHAPTER_ORDER.index(name)
        prev_link = (
            f'<a href="{DOC_URLS[CHAPTER_ORDER[idx - 1]]}">← Previous</a>'
            if idx > 0
            else ""
        )
        next_link = (
            f'<a href="{DOC_URLS[CHAPTER_ORDER[idx + 1]]}">Next chapter →</a>'
            if idx < len(CHAPTER_ORDER) - 1
            else '<a href="planner.html">Printable planner →</a>'
        )
        out = PAGE.format(
            title=html.escape(title),
            subtitle=subtitle,
            disclaimer=DISCLAIMER,
            body=body,
            prev_link=prev_link,
            next_link=next_link,
        )
        (SITE / DOC_URLS[name]).write_text(out, encoding="utf-8")
        print(f"built {name} -> site/{DOC_URLS[name]}")


if __name__ == "__main__":
    build()
    print("done.")
