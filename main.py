#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry (v1).

Writes one funny line a hopeless tech support agent gives a desperate
customer to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Gate (from the kit RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 199 characters, not only white space.
"""

import os
import sys

LINE = (
    "Good news: I turned it off and on again and it worked perfectly "
    "\u2014 on my computer. Yours is still broken, but mine feels brand new!"
)

MAX_CHARS = 199


def main() -> int:
    line = LINE
    # Gate validation, before writing anything.
    if not line.strip():
        print("error: entry is only white space", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= MAX_CHARS:
        print(
            f"error: entry is {len(line)} characters, gate is 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
