# Chapter 4: Grocery lists you can actually edit

The default way AI outputs a grocery list — a bulleted list inside a paragraph of prose — is the reason people give up. You can't check off a bullet inside a chat bubble. You can't move "buy more yogurt" to next week. This chapter fixes the format.

## The furniture of a good list

A list you'll actually use has four properties:

1. **Checklist format.** `- [ ]` checkbox lines, one item per line. Prints and pastes cleanly.
2. **Sectioned by store flow** (or at least by category). Produce together, dairy together.
3. **Carries metadata.** `Qty`, and a `next-time` marker for things you don't need *this* week but shouldn't forget.
4. **Editable outside the AI.** Plain text works in Notes apps, any text editor, or printed on paper.

## The list-generation prompt

This is **Prompt G-1** in the [prompt library](06-prompt-library.md):

```
Based on the 7-dinner plan we just discussed, make my grocery list.

Format rules — follow exactly:
- Output ONLY the list, no commentary before or after.
- Use checklist items in this form: - [ ] item — qty — note
- Group under these headings, in this order:
  BUY EVERY WEEK (our always-restocked safe foods)
  PRODUCE
  PROTEIN & DAIRY
  PANTRY
  FROZEN
  NEXT TIME (not this week — flagged for later)
- No nutrition or health advice.

Household size: 3. Budget note: prefer store brands where
a named brand doesn't matter (rice, beans, stock).
```

## Editing the list without touching the chat

Once you have the checklist text, treat it like a real file:

- **Paste into any notes app or text editor.** It's plain markdown — every line stays intact.
- **Check items off by replacing** `- [ ]` with `- [x]` (most markdown editors render this as a ticked box; on paper you just tick it).
- **Move items to `NEXT TIME`** by cutting the line and pasting it under that heading. That section is your standing memory, so the *next* prompt can pick it up.

## Re-using next week's list (the closing loop)

**Prompt G-2:**

```
Here is last week's grocery list, with my edits:

[paste the edited list]

Ignore anything marked [x]. Anything in NEXT TIME, include it
this week. Then, below the list, show what I should check in
my pantry before shopping (only the 5 most important items).
Remember: this is for my meal planning logistics only.
```

Notice what this does: the conversation now loops — plan → list → shop → edited list feeds the next plan. Your list file becomes the durable object; the chat with the AI is just the tool that edits it.

## Keeping the list yours: local-first options

| Option | What it is | Data travels where |
|---|---|---|
| Plain text file / paper | Zero tech | Nowhere |
| Phone notes app | Same text, synced by your chosen service | Your notes provider only |
| Free-tier cloud AI + pasted list | Full featured | The AI provider |
| [Ollama](https://ollama.com) ([Chapter 5](05-local-ai-with-ollama.md)) | Local AI on your own computer | Nowhere — fully offline capable |

You can mix freely: many people plan with a cloud free-tier AI using **vague** details ([Chapter 1](01-pantry-first-prompts.md)), then keep the actual lists as local text files. That's a perfectly good privacy posture.

## Format-drift fixes

AI models love to "improve" your format. When it starts embedding the list in prose again:

```
Format got lost. Re-generate ONLY the plain checklist, exactly
in the specified section order, one item per line, nothing else.
```

Persisting format instructions across a long chat usually works; if the chat gets too long, start fresh and re-paste the format block (that's what the prompt library is for).
