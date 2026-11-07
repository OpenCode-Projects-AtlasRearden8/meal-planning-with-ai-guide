# Chapter 7: Printable planner page

One page. Print it, stick it on the fridge, fill it in by hand. It's the "source of truth" once your AI chat has drafted the plan — and like everything in this manual, it carries a red line: **education only, not nutrition advice; that question belongs with your doctor or dietitian.**

> **How to print:** in the static site ([site index](../site/index.html)) open `planner.html` and print, or print this page from the plain-text version below. Both print cleanly on one sheet; the site version also fits A4.

## Design principles (so it survives real life)

- **Sunday-style planning** box at top — fill it whenever you plan; the day names are generic by design.
- **Short-order nights get their own rows** with a star, so a bad day is survivable at a glance.
- **A BACKUP row of its own** — the guilt-free escape hatch from [Chapter 2](02-short-order-nights.md).
- **Stash check column** — short-order nights live on the freezer stash; notice when it's empty.
- **Next week notes** — where NEXT TIME items from [Chapter 4](04-grocery-lists-you-can-edit.md) get copied by hand.

---

## The plain-text template

Copy this into any text editor or reprint it by hand.

```
        WEEK OF: ____________          HOUSEHOLD: ______ people

  PLANNED BY: ☐ me  ☐ me + AI (cloud)  ☐ me + AI (local, Ollama)
  Reminder: plans are logistics, not nutrition advice.

 -------------------------------------------------------------------
 | DAY        | DINNER PLAN (short)           | BUY? | STASH CHECK  |
 -------------------------------------------------------------------
 | MON        | ____________________________  | _    | ___________ |
 -------------------------------------------------------------------
 | TUE ★      | SHORT-ORDER: ________________ | _    | stash ok? Y/N|
 -------------------------------------------------------------------
 | WED        | ____________________________  | _    | ___________ |
 -------------------------------------------------------------------
 | THU ★      | SHORT-ORDER: ________________ | _    | stash ok? Y/N|
 -------------------------------------------------------------------
 | FRI        | ____________________________  | _    | ___________ |
 -------------------------------------------------------------------
 | SAT        | ____________________________  | _    | ___________ |
 -------------------------------------------------------------------
 | SUN        | ____________________________  | _    | ___________ |
 -------------------------------------------------------------------
 | ANY DAY    | BACKUP LADDER (fridge card):  |            |         |
 | (escape)   | L1 pantry  L2 one-pot         |            |         |
 |            | L3 frozen  L4 order out       |            |         |
 -------------------------------------------------------------------

  SAFE FOODS RESTOCK (buy every week):
  ☐ ________________  ☐ ________________  ☐ ________________
  ☐ ________________  ☐ ________________  ☐ ________________

  NEXT-WEEK NOTES (from NEXT TIME list and this week's lessons):
  __________________________________________________________
  __________________________________________________________

  ONE LINE OF GRATITUDE (optional, keeps it human):
  ______________________________ ♥
```

## Filling it in: a worked mini-example

- **TUE ★** = "dumpling bowl" card from [Chapter 2](02-short-order-nights.md); stash check: dumplings.
- **THU ★** = "plain pasta night" card; stash check: butter, cheese.
- **MON/WED/FRI/SUN** = pantry-first dinners copied from the chat's table, abbreviated ("chicken + rice + broc").
- **SAT** = eat-out night (Prompt #5 decided which recipe to drop).
- **Backup ladder** pre-written in small letters so no decision is needed at 6 p.m.
- **Next-week notes** = "out of soy sauce" + the two items bumped from NEXT TIME.

## Why hand-write it at all?

Because the chat is the tool and the paper is the *system*.scrollback gets lost; the fridge doesn't. The page also doubles as next week's prompt input — read Tuesday's row back into [Prompt G-2](04-grocery-lists-you-can-edit.md) and your plan loops itself.
