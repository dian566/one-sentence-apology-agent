"""One-sentence apology entry for the make.fun bounty.

Writes a single funny, human sentence of apology from an AI
assistant to the person it works for, into /output/entry.txt.
"""

import os

ENTRY = "I'm sorry I set your alarm for 7 PM instead of 7 AM and then proudly reported you slept through your own job interview."


def validate(entry: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, a single sentence."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(entry)}")
    if entry.strip().count(".") != 1 or not entry.strip().endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
