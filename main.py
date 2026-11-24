#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine to /output/entry.txt.
Deterministic, no network, no input. One line, at most 120 characters.
"""

import os

LABEL = (
    "WARNING: Do not exit before you enter. "
    "Passengers who meet themselves will be billed "
    "for both seats and one childhood."
)


def main() -> None:
    # Self-check against the competition gate: UTF-8, one line,
    # 1 to 120 characters, not only whitespace.
    text = LABEL.strip()
    assert 1 <= len(text) <= 120, f"label is {len(text)} chars, must be 1-120"
    assert "\n" not in text, "label must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
