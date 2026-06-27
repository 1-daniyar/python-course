# Practice 6 — Python File Handling and Built-in Functions

Working with files, directories, and Python's core built-in functions.
Every script is self-contained: it creates its own sample files/folders,
demonstrates the topic, and cleans up after itself.

## Repository Structure

```
Practice6/
├── file_handling/
│   ├── read_files.py          # read(), readline(), readlines(), iterating
│   ├── write_files.py         # modes w / a / x, write(), writelines()
│   └── copy_delete_files.py   # shutil copy, backup, safe delete
├── directory_management/
│   ├── create_list_dirs.py    # mkdir, makedirs, listdir, find by extension
│   └── move_files.py          # move/copy files, copytree
├── builtin_functions/
│   ├── map_filter_reduce.py   # map, filter, reduce, len/sum/min/max, conversions
│   └── enumerate_zip_examples.py  # enumerate, zip, unzip, dict(zip(...))
└── README.md
```

## How to Run

Each file runs on its own with no arguments and no extra packages
(standard library only):

```bash
python file_handling/read_files.py
python file_handling/write_files.py
python file_handling/copy_delete_files.py

python directory_management/create_list_dirs.py
python directory_management/move_files.py

python builtin_functions/map_filter_reduce.py
python builtin_functions/enumerate_zip_examples.py
```

## Topics Covered

**File handling**
- File modes `r`, `w`, `a`, `x`
- Reading: `read()`, `readline()`, `readlines()`, line-by-line iteration
- Writing & appending: `write()`, `writelines()`
- The `with` context manager (auto-closes files)
- Copy / backup / delete with `shutil` and `pathlib`

**Directory management**
- `os.getcwd()`, `os.mkdir()`, `os.makedirs()`, `os.listdir()`, `os.rmdir()`
- `pathlib.Path` for cross-platform paths (`iterdir`, `glob`, `rglob`)
- Finding files by extension
- Moving / copying files and whole trees (`shutil.move`, `copytree`, `rmtree`)

**Built-in functions**
- `len()`, `sum()`, `min()`, `max()`, `sorted()`
- `map()`, `filter()`, `reduce()` (from `functools`)
- `enumerate()`, `zip()`, unzip with `zip(*...)`, `dict(zip(...))`
- Type conversion: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `bool()`
- Type checking with `type()` and `isinstance()`

## Notes

- Paths use `pathlib.Path` and are built relative to each script
  (`Path(__file__).resolve().parent`), so the scripts work no matter
  which folder you run them from.
- Scripts delete the temporary files/folders they create, so running
  them repeatedly stays clean and nothing extra ends up in the repo.

## Push to GitHub

```bash
git add Practice6/
git commit -m "Add Practice6 - file handling and built-in functions examples"
git push origin main
```

## Resources

- [W3Schools File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [Python `os` module](https://docs.python.org/3/library/os.html)
- [Python `pathlib`](https://docs.python.org/3/library/pathlib.html)
- [Python built-in functions](https://docs.python.org/3/library/functions.html)
