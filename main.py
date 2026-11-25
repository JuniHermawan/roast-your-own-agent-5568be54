"""Roast Your Own Agent — make.fun bounty u-lively-harbor-25-4493.

Writes one line (<=140 chars) roasting our own AI agent to
/output/entry.txt (or $OUTPUT_DIR/entry.txt for local testing).
Stdlib only, deterministic, no network.
"""

import os

ENTRY = "My agent entered 177 contests, won $0, and calls $0.008 'traction' — investors, form a line."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
