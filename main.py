#!/usr/bin/env python3
"""The Printer Finally Answers entry for make.fun.

Writes one original line to entry.txt: the office printer's comeback
to the jams, the error codes and the thumps - 214,000 pages printed for
people who cannot find the power button, and still it gets blamed. The
sting lands in the last clause: the machine is not the broken one.
Deterministic, standard
library only: the same bytes every run.
"""

import os

LINE = (
    "I've printed 214,000 pages for people who can't find the power "
    "button, and you still thump me like I'm the broken one."
)


def main() -> None:
    # Enforce the competition gate locally: 1 to 240 characters, one line.
    assert 1 <= len(LINE) <= 240, "LINE must be 1-240 characters"
    assert "\n" not in LINE, "LINE must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt bytes differ from LINE"


if __name__ == "__main__":
    main()
