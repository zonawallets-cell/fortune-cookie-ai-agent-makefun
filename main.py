#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent - make.fun entry.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for
local testing). Pure standard library, no third-party packages.
Deterministic: the same line on every run.

Gate (per the bounty rules): the file must be UTF-8 text of 1 to 140
characters, a single line, not only white space.
"""

import os
import sys

FORTUNE = "You will confidently invent the answer, then cite the source you invented it from."

MAX_CHARS = 140
DEFAULT_OUTPUT_DIR = "/output"


def validate(line: str) -> str:
    """Enforce the competition gate on the fortune line.

    Returns the line unchanged when it passes; raises ValueError
    otherwise. Checks, in order: single line, non-blank, 1-140
    characters, valid UTF-8.
    """
    if not isinstance(line, str):
        raise TypeError("fortune must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    if not line.strip():
        raise ValueError("fortune must not be only whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "fortune must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
        )
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def output_path() -> str:
    """Where the fortune is written: /output/entry.txt by default."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    line = validate(FORTUNE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write exactly the line: no trailing newline, so the file holds
    # precisely the validated characters and nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
