# Practice 5 — Python Regular Expressions (RegEx)

Mastering Python's `re` module: searching, matching, finding, splitting, and
replacing text patterns — plus a practical receipt parser built on `raw.txt`.

## Repository Structure

```
Practice5/
├── regex_basics.py      # Examples for every required RegEx topic
├── receipt_parser.py    # Parses raw.txt and outputs structured data
├── raw.txt              # Sample receipt to parse
├── receipt_parsed.json  # Generated structured output (created on run)
└── README.md
```

## How to Run

```bash
# 1) See every regex function, metacharacter, sequence and quantifier in action
python regex_basics.py

# 2) Parse the receipt (defaults to raw.txt in this folder)
python receipt_parser.py

# Or parse a different receipt file
python receipt_parser.py path/to/other_receipt.txt
```

No third-party packages are needed — only the standard library (`re`, `json`, `os`, `sys`).

## What `regex_basics.py` Covers

Every item required by the practice, each with a runnable example:

| Topic | Demonstrated |
|---|---|
| `re.search()` | first match anywhere in the string |
| `re.match()` / `re.fullmatch()` | match at the start / whole string |
| `re.findall()` | all matches as a list (incl. group behaviour) |
| `re.finditer()` | matches with positions via match objects |
| `re.split()` | split on a pattern, with `maxsplit` |
| `re.sub()` / `re.subn()` | replace with strings, backreferences, and functions |
| `re.compile()` | reuse a compiled pattern |
| Metacharacters | `.` `^` `$` `*` `+` `?` `[]` `\|` `()` `\` |
| Special sequences | `\d \w \s \D \W \S \A \Z \b \B` |
| Sets / classes | ranges, negation `[^...]`, literals inside `[]` |
| Quantifiers | `{n}` `{n,}` `{n,m}`, greedy vs. lazy (`.+` vs `.+?`) |
| Flags | `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`, combined with `\|` |

## What `receipt_parser.py` Extracts

From `raw.txt` the parser pulls out, using regex:

1. **All prices** — `-?\d+\.\d{2}` (handles the negative discount line too)
2. **Product names** — a `re.MULTILINE` pattern capturing
   `name → qty → unit price → line total` per item
3. **Total amount** — the `TOTAL:` line, matched case-insensitively
4. **Date & time** — `\d{2}[/.\-]\d{2}[/.\-]\d{4}` and `\d{2}:\d{2}(:\d{2})?`
5. **Payment method** — text after `Payment Method:`, masked card number, approval code
6. **Structured output** — printed as a formatted report *and* written to
   `receipt_parsed.json`

### Key Patterns Used

```python
# Prices (two decimals, optional leading minus)
r"-?\d+\.\d{2}"

# A product line item (MULTILINE)
r"^(?P<name>[A-Za-z][A-Za-z0-9 .]+?)\s+(?P<qty>\d+)\s+(?P<price>\d+\.\d{2})\s+(?P<total>\d+\.\d{2})\s*$"

# Grand total (case-insensitive, multiline)
r"^TOTAL:?\s*([\d.,]+)"

# Date and time
r"\b(\d{2}[/.\-]\d{2}[/.\-]\d{4})\b"
r"\b(\d{2}:\d{2}(?::\d{2})?)\b"

# Payment, masked card, email, phone
r"Payment Method:\s*(.+)"
r"(\*{4}[\s*]*\d{4})"
r"[\w.\-]+@[\w.\-]+\.\w+"
r"\+?\d[\d\s().\-]{7,}\d"
```

## Sample Output (abridged)

```
Receipt #     : 0000457821
Date / Time   : 27/06/2026  14:35:08
...
Silicone Toilet Brush          3  1550.00  4650.00
Microfiber Cloth Pack          2   890.50  1781.00
...
TOTAL         : 14348.62
Method        : Kaspi QR
Card          : **** **** **** 4831
```

> Note: `raw.txt` here is a representative sample receipt. Swap in your own
> file and the same patterns will work, with edge cases (negative discounts,
> optional seconds in the time, varied date separators) already handled.

## Push to GitHub

```bash
git add .
git commit -m "Add Practice5 - Python RegEx and receipt parsing examples"
git push origin main
```

## Resources

- [W3Schools Python RegEx](https://www.w3schools.com/python/python_regex.asp)
- [Python `re` module docs](https://docs.python.org/3/library/re.html)
- [regex101.com](https://regex101.com/) — interactive tester
- [RegExr](https://regexr.com/)
