# Chapter 3: Picky-eater workarounds

Picky eaters are not a problem to solve in one prompt. They're a real constraint — like a small kitchen or a tight budget — and AI handle constraints well *if you state them precisely*. This chapter is about the wording that works.

## Rule 1: State the constraint, not the diagnosis

Which of these gets a usable answer?

- ❌ *"My kid is extremely picky with sensory issues, refuses all textures, has food anxiety..."*
- ✅ *"Plan dinners where each component can be served separately, no sauces mixed in, and one safe food available every night."*

The first prompt asks a chatbot to play therapist. The second asks it to do **logistics** — which is exactly what it's good at. Keep household health details out of the chat anyway (privacy — see [Chapter 5](05-local-ai-with-ollama.md)); operationally helpful descriptions are all you need.

## Rule 2: Prompt for "component meals," not "one dish"

The workhorse prompt (**Prompt P-1** in the [library](06-prompt-library.md)):

```
Plan 5 dinners for a household where some members eat "mixed
dishes" and some only eat plainly prepared, separate components.

For each dinner, give:
- BASE DISH: the family version
- DECONSTRUCTED VERSION: the same ingredients, kept separate
  and plain (no mixed sauces, no overlapping textures)
- SHARED PARTS: exactly which parts everyone eats the same way
- ONE SAFE FOOD present at every dinner

Keep cooking simple. One meal concept per night — I am NOT
cooking two separate dinners. Logistics only, no nutrition advice.
```

Example output shape:

| Night | Base dish | Deconstructed | Shared parts | Safe food |
|---|---|---|---|---|
| Mon | Chicken tacos | Tortilla + plain chopped chicken + cheese, each in own bowl | Tortillas, chicken, cheese | Tortilla |
| Tue | Pasta with sauce | Plain noodles + sauce on the side | Noodles | Noodles |

Same ingredients, one cooking session, two plating styles. That's the whole trick.

## Rule 3: Use the AI as a "new food translator"

A picky eater's safe list is long-term data. Instead of asking the AI to invent brand-new foods every week, ask it to **remix safe foods into new shapes**:

```
Here is a list of foods that reliably get eaten:
plain chicken, buttered noodles, cheese, tortillas, apples,
carrots, rice, scrambled eggs.

Without adding any new main foods, create 5 "same foods,
new arrangement" dinners — e.g., different assembly, different
cut, different dipping setup. Flag anything that changes
texture or temperature, since those are the riskiest changes.
```

This is dignified and effective: no "just get them to try kale," no nutrition lecture — just engineering with known-good parts.

## Rule 4: Let the AI build the "off-ramp" list

For escalation-prone moments, have your plan include a fallback ladder. **Template T-2** in the library:

```
Create a "fallback ladder" card for my fridge: 4 levels of
effort for tonight when the planned dinner is off the table:

Level 1: assemble-from-pantry (nothing cooked)
Level 2: one-pot, 10 minutes
Level 3: frozen shortcut
Level 4: order/backup plan, guilt-free

Use only foods we stock: [paste your staples list].
Each level: 2 options max, one sentence each.
Logistics only.
```

Print it, stick it inside a cupboard door. On a bad night you don't decide *whether* to improvise — you just pick a rung.

## Rule 5: Fold picky eats into the grocery list correctly

When generating your list ([Chapter 4](04-grocery-lists-you-can-edit.md)), make sure safe foods appear as **pantry staples**, not per-recipe garnishes:

```
In the grocery list, put the safe foods (tortillas, cheese,
apples, buttered-noodle supplies) in a "BUY EVERY WEEK" section
at the top. We restock them regardless of the meal plan.
```

## What NOT to ask

- **"How do I get my kid to eat vegetables?"** — that's feeding advice, outside this manual's lane, and the free AI will happily give you confident nonsense. Ask your pediatrician or feeding specialist what's right for your family.
- **"Is my child's eating pattern normal?"** — absolutely not a chatbot question. Healthcare professionals only.
- **Anything with the child's name, age, or medical details** pasted into a cloud chat. Keep it: "household includes picky eaters." That's all the AI needs.
