#!/usr/bin/env python3
"""Roast the Smart Fridge -- one-line entry writer.

Writes a single roast line (1-160 UTF-8 chars, one line, no trailing
newline) to /output/entry.txt. Deterministic, no network, no secrets.

The line was picked by an internal pairwise tournament over 10
candidate roasts, judged in the judge's own order: funny first, then
fresh/original angle, then specific to the gadget's real behaviour.
Winner: 9 wins out of 9 games.

Tournament (10 candidates, round-robin, judge criteria in order):
 1. milk-expiry irony                    2-7  (too close to the stock milk joke)
 2. needs an update to stay cold         0-9  (mild observation, no sting)
 3. judges 2 a.m. snacking, suggests salad  9-0  WINNER
 4. texts about eggs, shows ads for eggs 5-4  (good, but two-part and baggy)
 5. AI ordered ice cream "for the household" 6-3
 6. ice dispenser held hostage by firmware update 8-1
 7. fridge snitches midnight openings to my phone 1-8
 8. in-fridge camera sees me too         3-6  (creepy, weak roast)
 9. beeps about the door, never the smell 4-5
10. touchscreen froze on a $3,000 icebox 7-2  (clever wordplay, weaker sting)

Why #3 wins: a real behaviour (activity log + diet nudges), a fast
setup, and a sting that turns on the fridge itself -- it prescribes a
salad it has never contained. Fresh angle, no stock milk joke.
"""

import os

ENTRY = (
    "The smart fridge judges my 2 a.m. snacking out loud, then suggests "
    "a salad \u2014 from a fridge that has never once contained a salad."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")  # must be valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
