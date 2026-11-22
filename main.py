#!/usr/bin/env python3
"""news-image-20261121 entry (account 4): ship the composed front page.

This entrypoint copies the finished entry.png — the Saturday 21 November
2026 front page composed by compose_acct4.py (38 stories, 7 regions, flat
vector art, real Natural Earth coastlines on the map) — into the output
directory the grader reads ($MAKEFUN_OUTPUT_DIR/entry.png).

Stdlib only (os, shutil, sys). No network, no image work here: the PNG is
already built at authoring time, this script only delivers it, verifying
before and after the copy that the file is really there and non-empty.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("missing entry.png next to main.py\n")
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    src_size = os.path.getsize(src)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size <= 0 or size != src_size:
        sys.stderr.write("copied entry.png is empty or incomplete\n")
        sys.exit(1)
    print(f"entry.png copied ({size} bytes, matches source)")


if __name__ == "__main__":
    main()
