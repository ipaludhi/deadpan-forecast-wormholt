"""Deadpan Forecasts for Cities That Do Not Exist — one-line entry (program/v1, python3.13).

Writes a single original deadpan forecast line to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets that variable.
The line is fixed text, so every run writes identical bytes.
"""

import os
from pathlib import Path

ENTRY = "In Wormholt, the sun rises at 6:04 and sets at 6:05, having decided to keep its hours short; a full day of daylight is not expected this week."


def main() -> None:
    # Gate self-check (revision edit): the sealed gate wants 1-160 chars,
    # UTF-8 text, not only whitespace. Fail loudly instead of writing junk.
    assert 1 <= len(ENTRY) <= 160 and ENTRY.strip(), "entry fails the 1-160 char gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
