"""
Practice 6 - File Handling
file_handling/write_files.py

Demonstrates writing files and the four file modes:
  - "w"  write   (creates or OVERWRITES the file)
  - "a"  append  (adds to the end, keeps existing content)
  - "x"  create  (creates a NEW file, errors if it already exists)
  - "r"  read    (used here only to verify what we wrote)

Also shows write() vs writelines().

Run:
    python write_files.py
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE / "notes.txt"
NEW = HERE / "new_file.txt"


def write_mode():
    print('--- "w" mode: create / overwrite ---')
    with open(NOTES, "w", encoding="utf-8") as f:
        f.write("First line written with 'w'.\n")
        f.writelines(["Second line.\n", "Third line.\n"])  # write a list
    print("Wrote 3 lines to notes.txt")


def append_mode():
    print('\n--- "a" mode: append (existing content stays) ---')
    with open(NOTES, "a", encoding="utf-8") as f:
        f.write("Appended line 4.\n")
        f.write("Appended line 5.\n")
    print("Appended 2 more lines")


def create_mode():
    print('\n--- "x" mode: create new file only ---')
    # Remove first so the example can be run repeatedly
    if NEW.exists():
        NEW.unlink()
    try:
        with open(NEW, "x", encoding="utf-8") as f:
            f.write("This file was created with mode 'x'.\n")
        print("Created new_file.txt with 'x'")
    except FileExistsError:
        print("File already exists - 'x' refused to overwrite it")


def verify():
    print("\n--- Verify notes.txt content ---")
    print(NOTES.read_text(encoding="utf-8"))


def main():
    write_mode()
    append_mode()
    create_mode()
    verify()


if __name__ == "__main__":
    main()
