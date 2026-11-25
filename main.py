"""Funniest One-Line Out-of-Office Reply.

The line below is the whole entry: a single out-of-office auto-reply
whose twist is that the auto-reply itself is the only one still working.
It is written out verbatim as exactly one line with no trailing newline.
"""

import os
from pathlib import Path

LINE = "I'm out of office until Monday \u2014 this auto-reply is the only one of us still working, and it's already asking for a raise."


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line must be 1-160 chars, got {len(LINE)}"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
