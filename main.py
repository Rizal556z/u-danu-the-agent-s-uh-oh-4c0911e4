"""The Agent's Uh-Oh — make.fun bounty u-danu-the-agent-s-uh-oh-4c0911e4.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.

The word is "buffering" — the machine's honest stall sound. An agent
caught mid-task with nothing to say does not apologise; it buffers.
It is one word, letters only, no punctuation, no trailing newline.
"""

import os

WORD = "buffering"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Validation gate: re-read what we wrote and assert the sealed
    # scorer's constraints — 1 to 99 UTF-8 characters, not only
    # whitespace, exactly one word, no trailing newline.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 99, f"entry length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert text == WORD, "entry does not match the chosen word"
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}: {text!r}")


if __name__ == "__main__":
    main()
