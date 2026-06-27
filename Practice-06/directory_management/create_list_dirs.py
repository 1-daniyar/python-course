"""
Practice 6 - Directory Management
directory_management/create_list_dirs.py

Demonstrates directory operations with os and pathlib:
  - os.getcwd()            current working directory
  - os.mkdir()            create one directory
  - os.makedirs()         create nested directories
  - os.listdir()          list entries in a directory
  - Path.iterdir()        modern listing
  - finding files by extension with Path.glob() / rglob()
  - os.rmdir() and shutil.rmtree() for cleanup

Run:
    python create_list_dirs.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE / "demo_dir"


def show_cwd():
    print("--- Current working directory ---")
    print("os.getcwd():", os.getcwd())


def create_dirs():
    print("\n--- Create directories ---")
    # Start clean
    if ROOT.exists():
        shutil.rmtree(ROOT)

    os.mkdir(ROOT)                                  # single directory
    print("Created:", ROOT.name)

    os.makedirs(ROOT / "images" / "2026", exist_ok=True)   # nested
    os.makedirs(ROOT / "docs", exist_ok=True)
    print("Created nested: demo_dir/images/2026 and demo_dir/docs")

    # Drop a few sample files of different types
    (ROOT / "docs" / "report.txt").write_text("text", encoding="utf-8")
    (ROOT / "docs" / "data.csv").write_text("a,b,c", encoding="utf-8")
    (ROOT / "images" / "logo.png").write_bytes(b"\x89PNG")
    (ROOT / "images" / "2026" / "photo.png").write_bytes(b"\x89PNG")
    print("Added sample files")


def list_entries():
    print("\n--- List entries (os.listdir) ---")
    print(os.listdir(ROOT))

    print("\n--- List entries (Path.iterdir) ---")
    for p in sorted(ROOT.iterdir()):
        kind = "DIR " if p.is_dir() else "FILE"
        print(f"  [{kind}] {p.name}")


def find_by_extension():
    print("\n--- Find files by extension ---")
    # glob = current level only; rglob = recursive (all subfolders)
    png_files = list(ROOT.rglob("*.png"))
    print("All .png files (recursive):")
    for p in png_files:
        print("  ", p.relative_to(ROOT))

    txt_files = list(ROOT.rglob("*.txt"))
    print("All .txt files:", [str(p.relative_to(ROOT)) for p in txt_files])


def cleanup():
    print("\n--- Cleanup ---")
    # rmdir only removes EMPTY dirs; rmtree removes a whole tree
    shutil.rmtree(ROOT)
    print("Removed demo_dir and everything in it")


def main():
    show_cwd()
    create_dirs()
    list_entries()
    find_by_extension()
    cleanup()


if __name__ == "__main__":
    main()
