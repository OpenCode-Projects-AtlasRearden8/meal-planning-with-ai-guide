# Chapter 5: Keeping dietary data local with Ollama

Everything before this chapter works with a free cloud AI. If you'd rather your household's food details — safe foods, budgets, preferences, the full pantry list — **never leave your computer**, this chapter is for you.

## What Ollama is (in one friend-plain paragraph)

[Ollama](https://ollama.com) is a free app that runs AI chat models **on your own computer**. There's no account, no subscription, and no internet needed after you download the model. Your prompts, your lists, everything stays on your machine — chat happens the same way it would in a webpage, but the "server" is your laptop.

## What you need

- A computer: Windows, macOS, or Linux.
- **RAM:** 8 GB is the practical floor for smaller models; 16 GB is comfortable.
- **Disk space:** roughly 2–5 GB per model.
- Internet **once**, to download Ollama and the model file.

## Setup: five steps

### 1. Install Ollama

Download the installer from [ollama.com/download](https://ollama.com/download) and run it like any normal app.

### 2. Pull a model

Open a terminal (Terminal on macOS/Linux; PowerShell or Command Prompt on Windows) and type:

```bash
ollama run llama3.1:8b
```

The first run downloads the model (a few GB — this is the slow part). After it finishes, you land in a chat session. Type `/bye` to exit when you want.

> The model name `llama3.1:8b` is a good general-purpose choice for 16 GB machines. On an 8 GB machine try a smaller model, e.g. `ollama run llama3.2:3b`. Any of these is more than capable of meal-plan logistics.

### 3. Test it with the pantry prompt

In the chat (after `ollama run ...`), paste **Prompt #1** from the [prompt library](06-prompt-library.md). Because everything is local, you can now paste your *real* pantry list, your real household constraints, real safe foods — the text never goes anywhere.

### 4. (Optional) Write a persistent "household" prompt file

Ollama supports reusable system prompts. Save this as `household.txt` next to where you work:

```
You are a meal-planning assistant for my household. You:
- plan dinners, grocery lists, and short-order night cards
- always follow the output format I specify exactly
- never give nutrition, diet, or health advice — logistics only
- keep suggestions simple: one-pot or low-effort by default
- remember these household facts for this session:

[paste your own household facts here — this file stays on
your computer; do not paste it into any cloud AI chat]
```

Then run Ollama with it loaded:

```bash
ollama run llama3.1:8b "$(cat household.txt)"
```

(Works on macOS/Linux. On Windows PowerShell, `Get-Content household.txt -Raw` does the same.)

### 5. Where your data actually lives

- Model files: in Ollama's models folder (default `~/.ollama/models` on macOS/Linux; check [Ollama docs](https://github.com/ollama/ollama/blob/main/docs/faq.md) for Windows).
- Chat sessions: your `ollama run` conversations live in your terminal scrollback — not on any company server.
- Your files (lists, cards, `household.txt`): wherever you saved them.

Nothing in this flow requires an account or a network connection after download. Put your computer in airplane mode and it still works — that's the test.

## Honest tradeoffs

| | Cloud free tier | Local (Ollama) |
|---|---|---|
| Setup | None | One-time install |
| Smarts | Stronger models | Good-enough models for logistics |
| Speed | Fast server hardware | Depends on your computer |
| Privacy of details | Depends on provider data policies | Stays on your machine |
| Works offline | No | Yes, after download |

For meal-planning *logistics* — lists, templates, remixing — a local model genuinely is good enough. That's exactly why this manual's prompts are written as format-heavy, simple-reasoning tasks.

## When local is clearly the right call

- You want to paste real household details without second-guessing.
- You're building any of this into a family tool others will use.
- Your internet is unreliable and you want planning to always work.

## Careful notes

- **Model updates:** `ollama pull llama3.1:8b` re-downloads if a new build exists. Optional; the model you have works fine.
- **Disk hygiene:** models are a few GB each — remove one with `ollama rm <name>` if space matters.
- **Still education-only:** a local model will still drift toward diet talk if nudged. Keep the "logistics only" line in your system prompt — it works locally too.
