r"""
Practice 5 - Python Regular Expressions (RegEx)
================================================
regex_basics.py

This file demonstrates every topic required by the practice:
  - Metacharacters: . ^ $ * + ? [] | () \
  - Special sequences: \d \w \s \D \W \S \A \Z \b \B
  - Sets / character classes
  - Quantifiers: {n} {n,} {n,m}
  - re.search()  - find first match
  - re.findall() - find all matches
  - re.split()   - split a string
  - re.sub()     - replace patterns
  - re.match()   - match at the beginning
  - re.finditer()- iterate matches with positions
  - Flags: re.IGNORECASE, re.MULTILINE, re.DOTALL

Run it directly:
    python regex_basics.py
"""

import re


def section(title):
    """Print a labelled section header so the output is easy to read."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ----------------------------------------------------------------------
# 1. re.search() -- finds the FIRST match anywhere in the string
# ----------------------------------------------------------------------
def demo_search():
    section("1. re.search() - first match anywhere")
    text = "Order 0457 was placed at 14:35 for 4650 KZT"

    m = re.search(r"\d+", text)          # first run of digits
    print("First number:", m.group(), "at index", m.span())

    m = re.search(r"\d{2}:\d{2}", text)  # a HH:MM time
    print("Time found:", m.group())

    # search returns None when there is no match
    print("Has 'refund'?", bool(re.search(r"refund", text)))


# ----------------------------------------------------------------------
# 2. re.match() -- matches ONLY at the beginning of the string
# ----------------------------------------------------------------------
def demo_match():
    section("2. re.match() - match at the start only")
    print("Starts with 'Order'? ", bool(re.match(r"Order", "Order 0457")))
    print("Starts with 'Order'? ", bool(re.match(r"Order", "An Order 0457")))
    # fullmatch requires the WHOLE string to match
    print("Is '08152' all digits?", bool(re.fullmatch(r"\d+", "08152")))


# ----------------------------------------------------------------------
# 3. re.findall() -- returns a LIST of every match
# ----------------------------------------------------------------------
def demo_findall():
    section("3. re.findall() - all matches as a list")
    text = "Prices: 1550.00, 890.50, 3200.00 and 320.75 KZT"

    prices = re.findall(r"\d+\.\d{2}", text)   # number with 2 decimals
    print("All prices:", prices)

    words = re.findall(r"\b[A-Za-z]+\b", text) # all whole words
    print("All words:", words)

    # When the pattern has groups, findall returns the groups
    pairs = re.findall(r"(\d+)\.(\d{2})", text)
    print("(whole, decimal) pairs:", pairs)


# ----------------------------------------------------------------------
# 4. re.finditer() -- like findall but yields match objects (with positions)
# ----------------------------------------------------------------------
def demo_finditer():
    section("4. re.finditer() - matches with positions")
    text = "A1 B2 C3"
    for m in re.finditer(r"([A-Z])(\d)", text):
        print(f"  matched {m.group()!r} -> letter={m.group(1)} digit={m.group(2)} at {m.span()}")


# ----------------------------------------------------------------------
# 5. re.split() -- split a string on a pattern
# ----------------------------------------------------------------------
def demo_split():
    section("5. re.split() - split on a pattern")
    csv = "apple, banana;cherry|grape , melon"
    print("Split on , ; |:", re.split(r"\s*[,;|]\s*", csv))

    line = "one   two    three"
    print("Split on whitespace:", re.split(r"\s+", line))

    print("Split, keep max 2 pieces:", re.split(r",", "a,b,c,d", maxsplit=2))


# ----------------------------------------------------------------------
# 6. re.sub() -- replace matches (replacement may use a function/backrefs)
# ----------------------------------------------------------------------
def demo_sub():
    section("6. re.sub() - find and replace")
    text = "Call me at 727-350-1234 or 705-111-2222"

    masked = re.sub(r"\d", "#", text)
    print("Mask every digit:", masked)

    # Backreference: swap "first last" -> "last, first"
    print("Reorder name:", re.sub(r"(\w+)\s+(\w+)", r"\2, \1", "Aigerim Tulegenova"))

    # Replacement via a function: double every number
    doubled = re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "qty 3 and 4")
    print("Double numbers:", doubled)

    # subn also returns how many replacements were made
    new, count = re.subn(r"o", "0", "foobar boot")
    print(f"subn result: {new!r} ({count} replacements)")


# ----------------------------------------------------------------------
# 7. Metacharacters:  .  ^  $  *  +  ?  []  |  ()  \
# ----------------------------------------------------------------------
def demo_metacharacters():
    section("7. Metacharacters")
    print(". (any char)      :", re.findall(r"h.t", "hat hit hot hut h t"))
    print("^ (start)         :", bool(re.search(r"^The", "The Glory Store")))
    print("$ (end)           :", bool(re.search(r"KZT$", "Total 14348.62 KZT")))
    print("* (0 or more)     :", re.findall(r"ab*", "a ab abb abbb"))
    print("+ (1 or more)     :", re.findall(r"ab+", "a ab abb abbb"))
    print("? (0 or 1)        :", re.findall(r"colou?r", "color colour"))
    print("[] (a set)        :", re.findall(r"[aeiou]", "regular expression"))
    print("| (alternation)   :", re.findall(r"cat|dog", "a cat and a dog"))
    print("() (grouping)     :", re.findall(r"(ab)+", "ababab xx ab"))
    print("\\ (escape a dot)  :", re.findall(r"\d+\.\d+", "price 99.50 not 9950"))


# ----------------------------------------------------------------------
# 8. Special sequences:  \d \w \s \D \W \S \A \Z \b \B
# ----------------------------------------------------------------------
def demo_special_sequences():
    section("8. Special sequences")
    text = "Box_20L costs 750 KZT!"
    print(r"\d (digit)      :", re.findall(r"\d", text))
    print(r"\D (non-digit)  :", re.findall(r"\D", text)[:8], "...")
    print(r"\w (word char)  :", re.findall(r"\w+", text))
    print(r"\W (non-word)   :", re.findall(r"\W", text))
    print(r"\s (whitespace) :", len(re.findall(r"\s", text)), "spaces")
    print(r"\S (non-space)  :", re.findall(r"\S+", text))
    print(r"\A (start)      :", bool(re.search(r"\ABox", text)))
    print(r"\Z (end)        :", bool(re.search(r"!\Z", text)))
    print(r"\b (word edge)  :", re.findall(r"\b\w{3}\b", "the box is 750"))
    print(r"\B (non-edge)   :", re.findall(r"\Bo\B", "color tool moon"))


# ----------------------------------------------------------------------
# 9. Sets / character classes
# ----------------------------------------------------------------------
def demo_sets():
    section("9. Sets and character classes")
    text = "Receipt A12-b34 / C56_D78"
    print("[a-z]            :", re.findall(r"[a-z]+", text))
    print("[A-Z]            :", re.findall(r"[A-Z]", text))
    print("[0-9]            :", re.findall(r"[0-9]+", text))
    print("[A-Za-z0-9]      :", re.findall(r"[A-Za-z0-9]+", text))
    print("[^0-9] (negated) :", re.findall(r"[^0-9 ]+", text))
    print("[.+] literal     :", re.findall(r"[.+]", "1.5 + 2.5"))


# ----------------------------------------------------------------------
# 10. Quantifiers:  {n}  {n,}  {n,m}  and greedy vs lazy
# ----------------------------------------------------------------------
def demo_quantifiers():
    section("10. Quantifiers")
    print("{4}  exactly 4    :", re.findall(r"\d{4}", "12 345 6789 12345"))
    print("{2,} 2 or more    :", re.findall(r"\d{2,}", "1 22 333 4444"))
    print("{2,3} 2 to 3      :", re.findall(r"\d{2,3}", "1 22 333 4444"))
    # Greedy vs lazy
    html = "<a><b>"
    print("Greedy <.+>       :", re.findall(r"<.+>", html))
    print("Lazy   <.+?>      :", re.findall(r"<.+?>", html))


# ----------------------------------------------------------------------
# 11. Flags: re.IGNORECASE, re.MULTILINE, re.DOTALL
# ----------------------------------------------------------------------
def demo_flags():
    section("11. Flags")
    print("IGNORECASE :", re.findall(r"glory", "GLORY Glory glory", re.IGNORECASE))

    multiline = "first line\nsecond line\nthird line"
    print("MULTILINE  :", re.findall(r"^\w+", multiline, re.MULTILINE))

    print("DOTALL     :", bool(re.search(r"a.b", "a\nb", re.DOTALL)),
          "(. matches newline)")

    # Combine flags with |
    print("Combined   :", re.findall(r"^total", "TOTAL: 100\nTotal: 200",
                                     re.IGNORECASE | re.MULTILINE))


# ----------------------------------------------------------------------
# 12. Compiled patterns -- reuse a pattern efficiently
# ----------------------------------------------------------------------
def demo_compile():
    section("12. re.compile() - reuse a pattern")
    price_re = re.compile(r"\d+\.\d{2}")
    for line in ["Brush 1550.00", "Cloth 890.50", "no price here"]:
        m = price_re.search(line)
        print(f"  {line:20} -> {m.group() if m else 'no match'}")


def main():
    demo_search()
    demo_match()
    demo_findall()
    demo_finditer()
    demo_split()
    demo_sub()
    demo_metacharacters()
    demo_special_sequences()
    demo_sets()
    demo_quantifiers()
    demo_flags()
    demo_compile()
    print("\nAll regex demonstrations finished.\n")


if __name__ == "__main__":
    main()
