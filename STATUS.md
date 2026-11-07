# STATUS.md

**Project:** Meal Planning with Free AI — A Beginner's Manual
**Maintained by:** Asdale Dynamics, LLC
**Date:** 2026-11-07

## What was built

A documents-first beginner manual for weekly meal planning with free AI assistants, in the plain-English "like a friend would" style of the Asdale Dynamics series.

Content (all requested topics, education-only framing throughout — no nutrition or medical advice anywhere):

- `docs/index.md` — start-here: who it's for, five-minute version, ground rules, privacy overview
- `docs/01-pantry-first-prompts.md` — pantry-first planning method with base prompt and fix tips
- `docs/02-short-order-nights.md` — low-energy, ADHD-friendly short-order night template (fill-in prompt card + worked example + weekly planning rule)
- `docs/03-picky-eater-workarounds.md` — component-meal prompts, safe-food remix, fallback ladder, and what *not* to ask
- `docs/04-grocery-lists-you-can-edit.md` — checklist-format (`- [ ]`) list generation, NEXT TIME sections, week-to-week reloading
- `docs/05-local-ai-with-ollama.md` — fully-offline Ollama setup, persistent household prompt file, honest tradeoff table
- `docs/06-prompt-library.md` — 12+ copy-paste worked prompts with per-line "why" table
- `docs/07-printable-planner.md` — printable weekly planner (plain-text template + fill-in walkthrough)

Deliverables:

- `site/` — static site: hand-built `index.html`, `planner.html` (print-ready one-page planner with print stylesheet), `style.css`, plus all 7 chapters generated from `docs/` with chapter navigation
- `scripts/build.py` — dependency-free (stdlib only) markdown-to-HTML builder (headings, lists, GFM tables, fenced code, blockquotes, inline formatting, docs-relative link rewriting)
- `scripts/verify.py` — verification suite (see below)
- `README.md`, `LICENSE` (MIT, exact line `Copyright (c) 2026 Asdale Dynamics, LLC`)

Git repo initialized in this folder; single commit, plain message, existing identity, no Co-authored-by trailer.

## How to run it

```bash
# build the site from docs/
python3 scripts/build.py

# serve locally (no accounts, no keys, offline-capable)
python3 -m http.server 8000 --directory site
# open http://localhost:8000

# run the full verification suite
python3 scripts/verify.py
```

## Verification results

Run on 2026-11-07, all passing (`python3 scripts/verify.py` → `ALL CHECKS PASSED`):

- **Build runs cleanly** — 9 HTML pages generated (7 chapters + index + planner)
- **Idempotent build** — two consecutive builds produce byte-identical output
- **Balanced HTML** — every page parses with balanced tags (stdlib HTMLParser)
- **Link check** — no broken internal `href`/`src` across all pages (one initial failure, the external `faq.md` GitHub link being rewritten as local; fixed by skipping absolute URLs)
- **Disclaimer check** — every page contains the education-only disclaimer and the LLC credit
- **Renderer smoke test** — headings, inline styles, ordered/unordered lists, blockquotes, GFM tables, and fenced code all render correctly
- **HTTP smoke test** — `python3 -m http.server` returns 200 for index, planner, chapter, and CSS
- README/License checks — exact copyright line present in `LICENSE`

## Known gaps

- The static site is generated pages only — no search; navigation is chapter links.
- `build.py`'s markdown renderer is intentionally minimal (enough for these documents); it doesn't cover the full CommonMark/GFM spec (e.g., no nested lists, no reference links).
- `planner.html` uses client-side `window.print()`; a PDF export is not included.
- Local-AI chapter tested for instructions accuracy by structure, but model availability/versions on Ollama evolve — model name suggestions (`llama3.1:8b`, `llama3.2:3b`) may need a refresh over time.
- No automated prompt-output tests exist for the paid/free-tier chat behavior of external AI services (out of scope and out of reach for offline verification).
- Content is reviewed for "education only, never nutrition advice" as a manual check; future edits should re-run `python3 scripts/verify.py` and keep discipline in new prompts.
