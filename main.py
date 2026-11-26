# SPDX-License-Identifier: MIT
"""Laugh Track: The Crypto Trading Joke Contest — entry program.

Writes the winning line to /output/entry.txt.

The joke is the confession every trader recognises: the stop-loss was
set to protect the capital, then quietly moved to protect the ego. It
won a criteria-ordered tournament (the laugh first, then the truth of
trading life, then economy of the line) against nine original
candidates, including six seeded by OpenCode deepseek-v4.1-flash-free
on the Simular Box; the trading-journal runner-up ("This is it" /
"That was it") was tight but smaller, and the leverage and
long-term-investor lines leaned on shapes the field already knows.

Output is byte-exact, no trailing newline, inside the 1-200 char gate.
"""

from pathlib import Path

TEXT = (
    "I set a stop-loss to protect my capital, then moved it to "
    "protect my ego."
)
MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 200 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"
    encoded = text.encode("utf-8")
    assert encoded.decode("utf-8") == text, "gate: UTF-8 round-trip"
    assert len(encoded) <= MAX_CHARS, "gate: encoded bytes within limit"
    assert all(ord(ch) >= 32 for ch in text), "gate: no control characters"
    assert text.isascii(), "gate: ASCII only"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
