"""
Practice 6 - File Handling
file_handling/read_files.py

Demonstrates reading files:
  - open() with mode "r"
  - read()      -> whole file as one string
  - readline()  -> one line at a time
  - readlines() -> list of all lines
  - iterating over a file object line by line
  - the `with` context manager (auto-closes the file)

Run:
    python read_files.py
"""

from pathlib import Path

# Work next to this script so it runs from anywhere
HERE = Path(__file__).resolve().parent
SAMPLE = HERE / "sample.txt"


def make_sample():
    """Create a small sample file to read from."""
    SAMPLE.write_text(
        "Line 1: apples\n"
        "Line 2: bananas\n"
        "Line 3: cherries\n"
        "Line 4: dates\n",
        encoding="utf-8",
    )


def read_whole_file():
    print("--- read(): whole file as one string ---")
    with open(SAMPLE, "r", encoding="utf-8") as f:
        content = f.read()
    print(content)


def read_one_line():
    print("--- readline(): first two lines ---")
    with open(SAMPLE, "r", encoding="utf-8") as f:
        print(f.readline().strip())
        print(f.readline().strip())


def read_all_lines():
    print("\n--- readlines(): list of lines ---")
    with open(SAMPLE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("Number of lines:", len(lines))
    print("As a list:", [ln.strip() for ln in lines])


def iterate_lines():
    print("\n--- iterating line by line (memory friendly) ---")
    with open(SAMPLE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print(f"  {i}: {line.strip()}")


def main():
    make_sample()
    read_whole_file()
    read_one_line()
    read_all_lines()
    iterate_lines()


if __name__ == "__main__":
    main()
