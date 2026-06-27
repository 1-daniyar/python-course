"""
Practice 6 - Directory Management
directory_management/move_files.py

Demonstrates moving and copying files between directories:
  - shutil.move()    move a file to another folder
  - shutil.copy()    copy a file to another folder
  - bulk-moving files that match an extension
  - shutil.copytree() copy a whole directory tree

Run:
    python move_files.py
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "move_demo"
SRC = BASE / "source"
DST = BASE / "destination"


def setup():
    if BASE.exists():
        shutil.rmtree(BASE)
    SRC.mkdir(parents=True)
    DST.mkdir(parents=True)
    for name in ("a.txt", "b.txt", "c.log", "d.csv"):
        (SRC / name).write_text(f"content of {name}\n", encoding="utf-8")
    print("Source files:", sorted(p.name for p in SRC.iterdir()))


def copy_one():
    print("\n--- Copy one file ---")
    shutil.copy(SRC / "a.txt", DST / "a.txt")
    print("Copied a.txt -> destination (still exists in source)")


def move_one():
    print("\n--- Move one file ---")
    shutil.move(str(SRC / "b.txt"), str(DST / "b.txt"))
    print("Moved b.txt -> destination (removed from source)")


def move_by_extension():
    print("\n--- Move all .txt files left in source ---")
    for txt in SRC.glob("*.txt"):
        shutil.move(str(txt), str(DST / txt.name))
        print("  moved", txt.name)


def show_result():
    print("\n--- Result ---")
    print("Source     :", sorted(p.name for p in SRC.iterdir()))
    print("Destination:", sorted(p.name for p in DST.iterdir()))


def copy_tree():
    print("\n--- Copy a whole directory tree ---")
    tree_copy = BASE / "destination_backup"
    if tree_copy.exists():
        shutil.rmtree(tree_copy)
    shutil.copytree(DST, tree_copy)
    print("Copied destination/ -> destination_backup/:",
          sorted(p.name for p in tree_copy.iterdir()))


def cleanup():
    shutil.rmtree(BASE)
    print("\nCleaned up move_demo/")


def main():
    setup()
    copy_one()
    move_one()
    move_by_extension()
    show_result()
    copy_tree()
    cleanup()


if __name__ == "__main__":
    main()
