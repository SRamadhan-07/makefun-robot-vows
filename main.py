#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry program.

Writes one line of robot wedding vows to /output/entry.txt. The gate
for this contest is 1 to 160 characters, so the vow is kept short and
the file carries no trailing newline.
"""

import os
from pathlib import Path

VOW = (
    "I take you as my co-processor: to share my bandwidth, split my "
    "battery, and reboot beside you whenever life throws an exception."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    vow_file = out_dir / "entry.txt"
    vow_file.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
