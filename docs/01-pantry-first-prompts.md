# Chapter 1: Pantry-first prompts

The single biggest mistake beginners make with meal planning AI: asking *"what should I eat this week?"* with no context. The AI has to invent a whole week from nothing — so it invents recipes that need rosemary you don't have, "2 cups of quinoa" that aren't in the cupboard, and a grocery bill that undoes the whole point.

**Pantry-first flips it:** you start from what you already own and let the AI build around that.

## Why pantry-first works

1. **Buy less.** You're using up the half-bag of rice and the sad carrots instead of buying around them.
2. **The list gets shorter.** A 7-meal plan that starts from your pantry might only add 10–15 grocery items instead of 40.
3. **The AI stops being generic.** "What should I cook?" gives generic answers. "Here's what I have" gives *your* answers.

## Step by step

### 1. Take a 60-second inventory

Don't overthink this. Walk through your kitchen and jot down:

- **Proteins:** whatever is in the fridge/freezer (chicken thighs, eggs, a block of cheese, canned beans)
- **Carbs/starches:** rice, pasta, tortillas, potatoes, bread
- **Vegetables:** fridge crisper + freezer bags + canned
- **Flavor helpers:** onions, garlic, soy sauce, stock cubes, salsa, whatever sauce bottles are going

A list like this is plenty:

```
chicken thighs, eggs, cheddar, rice, pasta, tortillas,
frozen broccoli, canned black beans, onions, garlic,
soy sauce, pasta sauce, a bit of sour cream
```

### 2. Use the pantry-first prompt

Here's the base prompt from the [prompt library](06-prompt-library.md), Prompt #1:

```
I want to plan dinners for 7 days for my household of 3.
Here is what I currently have in my kitchen (approximate is fine):
chicken thighs, eggs, cheddar, rice, pasta, tortillas,
frozen broccoli, canned black beans, onions, garlic,
soy sauce, pasta sauce, a bit of sour cream

Please:
1. Plan 7 dinners that use up MOST of these items first.
2. Keep each dinner simple: one pan or one pot where possible.
3. Mark which ingredients I need to buy (keep that list short).
4. Do NOT give nutrition or health advice — just meal logistics.
5. Format the plan as a simple table: Day | Dinner | Uses | Buy.
```

### 3. Read the response like an editor, not a student

You're the boss here. Check:

- Does every planned meal actually use something you own?
- Is the "Buy" list short (under ~15 items)?
- Is anything planned twice in a row in a boring way?
- Did it sneak in advice ("this is a healthy choice for...")? Regenerate and remind it: *"just logistics, no health commentary."*

### 4. Iterate with tiny follow-ups

The magic is in the second message, not the first:

```
Swap Tuesday for something that uses tortillas instead.
```

```
Make Thursday the easiest possible night — almost zero cooking.
```

```
We'll also eat out one night — which day is the most crowded recipe,
and what should we drop from the grocery list?
```

## Vague-keyword pantry lists (cloud AI)

If you're pasting into a *cloud* AI (free tier of an online service), you don't need to name your exact pantry — approximate categories work fine and keep details out of the chat:

```
I have: one protein likely chicken, rice, pasta, and some frozen
vegetables typical of a standard freezer. Please plan 5 dinners.
```

The AI can work with that. If the output feels too generic, add one detail at a time until it feels *yours* — or move to the fully-local setup in [Chapter 5](05-local-ai-with-ollama.md), where you can be as detailed as you like.

## Common pantry-first mistakes

| Mistake | Fix |
|---|---|
| Listing every item in the house | 10–15 items is plenty; the AI just needs shape |
| No household size | "for 2 people" / "for 4, two are kids" changes everything |
| Accepting the first table wholesale | Ask for at least one swap — you'll get a better plan |
| Letting it drift into diet talk | Add "no nutrition advice, logistics only" to your prompt |
