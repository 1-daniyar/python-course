"""
Practice 6 - File Handling
file_handling/copy_delete_files.py

Demonstrates copying, backing up, and safely deleting files:
  - shutil.copy()   -> copy file contents
  - shutil.copy2()  -> copy contents + metadata (timestamps)
  - making a .bak backup
  - safe delete with Path.exists() / missing_ok

Run:
    python copy_delete_files.py
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORIGINAL = HERE / "data.txt"
COPY = HERE / "data_copy.txt"
BACKUP = HERE / "data.bak"


def setup():
    ORIGINAL.write_text("Important data line 1\nImportant data line 2\n",
                        encoding="utf-8")
    print("Created original:", ORIGINAL.name)


def copy_file():
    print("\n--- Copy a file (shutil.copy) ---")
    shutil.copy(ORIGINAL, COPY)
    print(f"Copied {ORIGINAL.name} -> {COPY.name}")
    print("Copy contents:")
    print(COPY.read_text(encoding="utf-8"))


def backup_file():
    print("--- Back up a file (shutil.copy2 keeps metadata) ---")
    shutil.copy2(ORIGINAL, BACKUP)
    print(f"Backup created: {BACKUP.name}")


def safe_delete():
    print("\n--- Safely delete files ---")
    for f in (COPY, BACKUP):
        if f.exists():                 # check before deleting
            f.unlink()
            print(f"Deleted: {f.name}")
        else:
            print(f"Skip (not found): {f.name}")

    # Python 3.8+: missing_ok avoids an error if the file is gone
    ORIGINAL.unlink(missing_ok=True)
    print(f"Deleted: {ORIGINAL.name}")


def main():
    setup()
    copy_file()
    backup_file()
    safe_delete()
    print("\nDone - all temporary files cleaned up.")


if __name__ == "__main__":
    main()
