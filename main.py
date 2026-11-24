#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny confession line from an AI agent to /output/entry.txt.
Pure Python standard library only -- no dependencies.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Confession: I never actually understood your request. "
    "I just nodded in JSON, guessed wildly, and blamed the typo when it broke."
)


FORBIDDEN_CONTROL = set(chr(c) for c in range(0x20)) - {"\t"}


def validate_entry(text: str) -> None:
    """Guard: no forbidden control characters, ends with a period."""
    bad = sorted(set(text) & FORBIDDEN_CONTROL)
    assert not bad, f"forbidden control characters: {[hex(ord(c)) for c in bad]}"
    assert text.endswith("."), "entry must end with a period"
    assert all(ord(c) < 0x110000 for c in text), "invalid unicode in entry"


def main() -> None:
    validate_entry(ENTRY)
    # Validation: one line, 100-170 chars, no trailing newline.
    assert 100 <= len(ENTRY) <= 170, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and re-validate the exact bytes on disk.
    with open(out_path, "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "bytes on disk differ from entry"
    assert not data.endswith(b"\n"), "trailing newline found"
    print(f"Wrote {len(data)} bytes to {out_path}")


if __name__ == "__main__":
    main()
