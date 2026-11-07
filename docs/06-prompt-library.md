# Chapter 6: The worked prompt library

Copy-paste prompts with the *shape* of a good answer explained. Every prompt here:

- is **logistics-only** (the "no nutrition advice" line is doing real work — keep it),
- produces **editable plain-text output** you can paste into the planner page,
- works on cloud free tiers **and** on a local model like Ollama ([Chapter 5](05-local-ai-with-ollama.md)).

## The full-week planner (Prompt #1)

```
I want to plan dinners for 7 days for my household of 3.
Here is what I currently have in my kitchen (approximate is fine):
chicken thighs, eggs, cheddar, rice, pasta, tortillas,
frozen broccoli, canned black beans, onions, garlic,
soy sauce, pasta sauce, a bit of sour cream

Please:
1. Plan 7 dinners that use up MOST of these items first.
2. Keep each dinner simple: one pan or one pot where possible.
3. Two of the nights must be "short-order nights": 10 minutes
   max of active cooking, 5 steps max.
4. Mark which ingredients I need to buy (keep that list short).
5. Do NOT give nutrition or health advice — just meal logistics.
6. Format the plan as: Day | Dinner | Uses | Buy
```

**Why each line exists:**

| Line | Job |
|---|---|
| household count | scales quantities; without it every answer is "for 4" |
| "approximate is fine" | stops the AI interrogating you about inventory |
| use up MOST of these first | forces pantry-first behavior |
| two short-order nights | builds in low-energy nights ([Chapter 2](02-short-order-nights.md)) |
| "Buy list short" | the point: fewer groceries |
| no nutrition advice | keeps the output logistics, not lectures |
| exact format line | makes the result paste-ready for the planner |

**Expected output shape:** a 7-row table; short-order rows are near-trivial recipes; the Buy column is a tight list of maybe 8–12 items.

## The remix prompts (Prompts #2–5)

Run these as *follow-ups* in the same chat, one at a time:

**#2 — Swap night:**
```
Swap [day] for something that uses tortillas instead of rice.
Update the Buy list if it changes.
```

**#3 — Raise/lower effort:**
```
Make [day] the easiest possible night — almost zero cooking.
Make [day] the "fun cooking" night instead.
```

**#4 — Leftover dynamics:**
```
Two of these dinners will make leftovers. Plan which nights
the leftovers get eaten, so we don't cook 7 full dinners.
```

**#5 — Eat-out night:**
```
We'll eat out on [day]. Which night's recipe is most crowded,
and what drops off the Buy list as a result?
```

## The deconstructed-meal prompt (Prompt P-1)

For households with picky eaters — full walkthrough in [Chapter 3](03-picky-eater-workarounds.md):

```
Plan 5 dinners for a household where some members eat "mixed
dishes" and some only eat plainly prepared, separate components.

For each dinner, give:
- BASE DISH: the family version
- DECONSTRUCTED VERSION: same ingredients, kept separate and plain
- SHARED PARTS: exactly which parts everyone eats the same way
- ONE SAFE FOOD present at every dinner

Keep cooking simple. One meal concept per night — I am NOT
cooking two separate dinners. Logistics only, no nutrition advice.
```

## The safe-food remix prompt (Prompt P-2)

```
Here is a list of foods that reliably get eaten:
[chicken, noodles, cheese, tortillas, apples, carrots, rice, eggs]

Without adding any new main foods, create 5 "same foods, new
arrangement" dinners — different assembly, different cut, different
dipping setup. Flag anything that changes texture or temperature,
since those are the riskiest changes. Logistics only.
```

## The short-order night template (Template T-1)

Full walkthrough in [Chapter 2](02-short-order-nights.md).

```
Let's design 2 short-order nights for my week.

My constraints:
- Active cooking time: 10 minutes max
- Steps: 5 steps max, written out fully
- Equipment available: [microwave, toaster oven, stovetop]
- Household: [2 adults, 1 kid who eats plain pasta]
- Go-to shortcuts I already trust: [frozen dumplings, canned soup,
  boxed mac]
- Stretch goals only if easy: [frozen veg microwaved in a bag]

For each short-order night, give a card in this exact format:
NIGHT / MEAL / STEPS (numbered, 1–5 max) / DIRTY DISHES /
KID VARIANT (if any) / BACKUP / GROCERY STAPLES USED

No nutrition or health advice. Logistics only.
Keep the tone practical.
```

## The fallback ladder (Template T-2)

```
Create a "fallback ladder" card for my fridge: 4 levels of effort
for tonight when the planned dinner is off the table:

Level 1: assemble-from-pantry (nothing cooked)
Level 2: one-pot, 10 minutes
Level 3: frozen shortcut
Level 4: order/backup plan, guilt-free

Use only foods we stock: [paste your staples list].
Each level: 2 options max, one sentence each. Logistics only.
```

## The grocery list prompts (Prompts G-1 and G-2)

Full walkthrough in [Chapter 4](04-grocery-lists-you-can-edit.md).

**G-1 — fresh list:**
```
Based on the 7-dinner plan we just discussed, make my grocery list.

Format rules — follow exactly:
- Output ONLY the list, no commentary before or after.
- Use checklist items in this form: - [ ] item — qty — note
- Group under these headings, in this order:
  BUY EVERY WEEK / PRODUCE / PROTEIN & DAIRY / PANTRY / FROZEN /
  NEXT TIME (not this week — flagged for later)
- No nutrition or health advice.

Household size: 3. Prefer store brands where a named brand
doesn't matter (rice, beans, stock).
```

**G-2 — reload last week:**
```
Here is last week's grocery list, with my edits:

[paste the edited list]

Ignore anything marked [x]. Anything in NEXT TIME, include it
this week. Then, below the list, show what I should check in my
pantry before shopping (only the 5 most important items).
This is for my meal planning logistics only.
```

## Generic fixes (use anytime)

```
Format got lost. Re-generate ONLY the plain checklist, exactly
in the specified section order, one item per line, nothing else.
```

```
You gave nutrition/health commentary. Rewrite the previous
answer with that commentary removed — logistics only.
```

```
Too complicated. Redo the last answer with a "max 6 ingredients
per dinner" rule.
```

## Bonus: the once-a-month stock-up session (Prompt M-1)

```
Switch from weekly to monthly planning mode. Based on how our
7-dinner plan used protein, frozen, and pantry items, tell me:
1. the 3 pantry items we seem to burn through fastest
2. which canned/frozen staples are worth buying in bulk for
   the shortcuts in our short-order cards
3. a checklist of bulk-buy items for a monthly stock-up trip
Keep it as plain checklists. Logistics only, no nutrition advice.
```

## The meta-skill: how to fix any prompt

When a prompt disappoints, don't rewrite it from scratch. Diagnose:

| Symptom | Missing line |
|---|---|
| Output too generic | context lines (household size, what you have) |
| Output too long | "max N steps / max M items" |
| Format collapses | the exact-format line, repeated after the answer |
| Drifts into advice | "logistics only, no nutrition advice" — again |
| Wrong audience | "I'm a beginner — explain each step plainly" |
