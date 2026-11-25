#!/usr/bin/env python3
"""One-line office joke entry for the make.fun bounty.

Prints exactly the entry text to stdout, with no trailing newline.
"""

import os
import sys

ENTRY = (
    "The printer only jams when the document is urgent, the boss is watching, "
    "and you've already told everyone you fixed it."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition's constraints on the entry text."""
    if not text:
        raise ValueError("entry text must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main() -> int:
    validate(ENTRY)
    # Stage the entry to a temp file and read it back to verify it is
    # byte-identical before printing it.
    import tempfile

    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False, suffix=".txt"
    ) as tmp:
        tmp.write(ENTRY)
        staged_path = tmp.name
    try:
        with open(staged_path, "r", encoding="utf-8") as fh:
            staged = fh.read()
    finally:
        os.unlink(staged_path)
    if staged != ENTRY:
        raise RuntimeError("staged entry does not match the entry text")
    try:
        sys.stdout.write(ENTRY)
        sys.stdout.flush()
    except (BrokenPipeError, OSError):
        out_path = os.environ.get("MAKEFUN_OUTPUT") or "./output/entry.txt"
        parent = os.path.dirname(out_path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
