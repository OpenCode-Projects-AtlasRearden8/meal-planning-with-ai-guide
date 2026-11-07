# Meal Planning with Free AI — A Beginner's Manual

*A beginner manual for weekly meal planning with free AI assistants, by Asdale Dynamics, LLC.*

Plain-English, step-by-step, never condescending — explained like a friend would. This guide teaches complete beginners (including nurses, parents, and anyone running a household) how to use free AI chat tools to plan a week of dinners with less stress, less shopping, and zero guilt.

## What's inside

- **Pantry-first prompts** — plan from what you already own, so the grocery list shrinks
- **Short-order nights** — a fill-in template for planned low-effort nights (ADHD-friendly by design; two easy nights anchor every plan)
- **Picky-eater workarounds** — "component meal" prompts that respect picky eaters without cooking two dinners
- **Grocery list generation you can actually edit** — checklist-format output with NEXT TIME sections that loop week to week
- **Keeping dietary data local with Ollama** — run AI fully offline on your own computer so household details never leave home
- **A printable weekly planner page** — one page for the fridge
- **A worked prompt library** — copy-paste prompts with expected output shapes and fix-it-anytime recipes

Read the manual in [docs/](docs/), starting with [docs/index.md](docs/index.md).

## Who it's for

- Anyone who wants dinners decided before 5 p.m. panic mode
- Beginners curious about free AI tools (ChatGPT, Claude, Gemini free tiers) or local AI (Ollama)
- Households with picky eaters, low-energy nights, or both

## Repository layout

```
docs/           The manual, chapter by chapter (plain markdown)
site/           Static site: index, all chapters, print-ready planner page
scripts/        build.py (docs -> site) and verify.py (full check suite)
```

This guide is intentionally distinct from other ASDALE DYNAMICS projects: it is a **documents-first manual** (no web app to install, no tool to configure).

## How to run it

Build the static site from the markdown source:

```bash
python3 scripts/build.py
```

Then browse it however you like:

```bash
python3 -m http.server 8000 --directory site
# open http://localhost:8000
```

No accounts, no API keys, no network access needed — the site is fully static and works offline.

Verify everything (build, HTML structure, links, disclaimers, renderer):

```bash
python3 scripts/verify.py
```

## Ground rules

- **Education only.** This manual teaches meal-planning *logistics*. It contains no nutrition advice and no medical guidance; prompts are deliberately written to keep AI on logistics. For dietary decisions, talk to your doctor or a registered dietitian.
- **Local-first and privacy-conscious.** Default prompts are deliberately vague so cloud chats never need your household details; the Ollama chapter shows a fully offline alternative.
- **No secrets, ever.** Nothing in this repo is an API key, account credential, or personal data.

## About Asdale Dynamics, LLC

Meal Planning with Free AI is part of the beginner-friendly AI series by **Asdale Dynamics, LLC** — the publishing home of Dylan Asdale (registered nurse turned AI author, wrote *The Massive AI Manual*). The LLC publishes plain-English AI guides, books, and practical tools: beginner AI education, open-source apps and templates, local-LLM utilities, MCP servers, agent skills, and accessible life-admin helpers.

Companion manual: *The Massive AI Manual*. Hub site: dylanasdale.github.io.

## License

MIT — see [LICENSE](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC
