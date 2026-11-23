"""Copy the pre-written patch note into the output directory.

Stdlib only: the grader runs this with `python3 -P -s` in a sandbox with
no network and a read-only repo, so this file imports nothing beyond
`os` and `shutil` and writes nothing into its own directory.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    print("wrote " + dst)


if __name__ == "__main__":
    main()
