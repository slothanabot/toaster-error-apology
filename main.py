#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry (account B).

Writes a single toaster error line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, no network, no model calls.

The line (85 chars, limit 120):
    E14: Bread declined to participate. Remove it gently and pretend this never happened.

Angle: consent. The bread refuses to be toasted, and the toaster — a
small appliance that has seen things — asks the owner to quietly pretend
none of it happened. Deadpan, one voice, lands on a single read.
"""

import os
import sys

LINE = "E14: Bread declined to participate. Remove it gently and pretend this never happened."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    # MAKEFUN_OUTPUT_DIR names a directory; a bare file path is also tolerated.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
