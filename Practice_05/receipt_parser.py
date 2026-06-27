"""
Practice 5 - Receipt Parsing with RegEx
========================================
receipt_parser.py

Reads `raw.txt` and uses regular expressions to extract:
  1. All prices on the receipt
  2. All product names (with quantity and line total)
  3. The total amount
  4. Date and time
  5. Payment method
  6. A structured JSON / formatted-text output

Run it:
    python receipt_parser.py            # parses raw.txt next to this file
    python receipt_parser.py other.txt  # parse a different file
"""

import re
import os
import sys
import json


# ----------------------------------------------------------------------
# Reading the file
# ----------------------------------------------------------------------
def read_receipt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ----------------------------------------------------------------------
# 1. Extract all prices
#    Matches numbers with exactly two decimals: 1550.00, 890.50, -1423.48
# ----------------------------------------------------------------------
def extract_prices(text):
    prices = re.findall(r"-?\d+\.\d{2}", text)
    return [float(p) for p in prices]


# ----------------------------------------------------------------------
# 2. Extract product line items
#    Each item line looks like:
#        Silicone Toilet Brush      3    1550.00   4650.00
#    Pattern: NAME (letters/digits/spaces) QTY UNIT_PRICE LINE_TOTAL
# ----------------------------------------------------------------------
def extract_items(text):
    item_re = re.compile(
        r"^(?P<name>[A-Za-z][A-Za-z0-9 .]+?)\s+"  # product name (lazy)
        r"(?P<qty>\d+)\s+"                          # quantity
        r"(?P<price>\d+\.\d{2})\s+"                 # unit price
        r"(?P<total>\d+\.\d{2})\s*$",               # line total
        re.MULTILINE,
    )
    items = []
    for m in item_re.finditer(text):
        items.append({
            "name": m.group("name").strip(),
            "qty": int(m.group("qty")),
            "unit_price": float(m.group("price")),
            "line_total": float(m.group("total")),
        })
    return items


# ----------------------------------------------------------------------
# 3. Extract the grand total
#    Looks for the TOTAL line, ignoring case, e.g. "TOTAL:  14348.62 KZT"
# ----------------------------------------------------------------------
def extract_total(text):
    m = re.search(r"^TOTAL:?\s*([\d.,]+)", text, re.IGNORECASE | re.MULTILINE)
    if m:
        return float(m.group(1).replace(",", ""))
    return None


def extract_subtotal_vat_discount(text):
    """Bonus: pull subtotal, discount and VAT if present."""
    def grab(label):
        m = re.search(rf"{label}.*?(-?\d+\.\d{{2}})", text, re.IGNORECASE)
        return float(m.group(1)) if m else None
    return {
        "subtotal": grab(r"Subtotal"),
        "discount": grab(r"Discount"),
        "vat": grab(r"VAT"),
    }


# ----------------------------------------------------------------------
# 4. Extract date and time
#    Date: 27/06/2026 (also accepts - or . separators)
#    Time: 14:35:08 or 14:35
# ----------------------------------------------------------------------
def extract_datetime(text):
    date_m = re.search(r"\b(\d{2}[/.\-]\d{2}[/.\-]\d{4})\b", text)
    time_m = re.search(r"\b(\d{2}:\d{2}(?::\d{2})?)\b", text)
    return {
        "date": date_m.group(1) if date_m else None,
        "time": time_m.group(1) if time_m else None,
    }


# ----------------------------------------------------------------------
# 5. Extract payment method
#    Captures the text after "Payment Method:" and a masked card if present
# ----------------------------------------------------------------------
def extract_payment(text):
    method_m = re.search(r"Payment Method:\s*(.+)", text, re.IGNORECASE)
    card_m = re.search(r"(\*{4}[\s*]*\d{4})", text)
    approval_m = re.search(r"Approval Code:\s*(\d+)", text, re.IGNORECASE)
    return {
        "method": method_m.group(1).strip() if method_m else None,
        "card": card_m.group(1).strip() if card_m else None,
        "approval_code": approval_m.group(1) if approval_m else None,
    }


# ----------------------------------------------------------------------
# Extra metadata (store, receipt number, email) - shows more regex use
# ----------------------------------------------------------------------
def extract_metadata(text):
    receipt_m = re.search(r"Receipt #?:?\s*(\d+)", text, re.IGNORECASE)
    email_m = re.search(r"[\w.\-]+@[\w.\-]+\.\w+", text)
    phone_m = re.search(r"\+?\d[\d\s().\-]{7,}\d", text)
    return {
        "receipt_number": receipt_m.group(1) if receipt_m else None,
        "email": email_m.group(0) if email_m else None,
        "phone": phone_m.group(0).strip() if phone_m else None,
    }


# ----------------------------------------------------------------------
# Assemble everything into one structured dict
# ----------------------------------------------------------------------
def parse_receipt(text):
    items = extract_items(text)
    calc_total = round(sum(i["line_total"] for i in items), 2)
    return {
        "metadata": extract_metadata(text),
        "datetime": extract_datetime(text),
        "items": items,
        "all_prices": extract_prices(text),
        "amounts": extract_subtotal_vat_discount(text),
        "total_on_receipt": extract_total(text),
        "items_line_total": calc_total,
        "payment": extract_payment(text),
    }


# ----------------------------------------------------------------------
# Pretty printer for the terminal
# ----------------------------------------------------------------------
def print_report(data):
    print("=" * 50)
    print("           PARSED RECEIPT REPORT")
    print("=" * 50)

    meta = data["metadata"]
    print(f"Receipt #     : {meta['receipt_number']}")
    print(f"Date / Time   : {data['datetime']['date']}  {data['datetime']['time']}")
    print(f"Phone         : {meta['phone']}")
    print(f"Email         : {meta['email']}")

    print("\nITEMS")
    print("-" * 50)
    print(f"{'Product':28}{'Qty':>4}{'Unit':>9}{'Total':>9}")
    print("-" * 50)
    for it in data["items"]:
        print(f"{it['name']:28}{it['qty']:>4}{it['unit_price']:>9.2f}{it['line_total']:>9.2f}")
    print("-" * 50)

    amt = data["amounts"]
    if amt["subtotal"] is not None:
        print(f"Subtotal      : {amt['subtotal']:.2f}")
    if amt["discount"] is not None:
        print(f"Discount      : {amt['discount']:.2f}")
    if amt["vat"] is not None:
        print(f"VAT           : {amt['vat']:.2f}")
    print(f"TOTAL         : {data['total_on_receipt']:.2f}")
    print(f"(sum of lines : {data['items_line_total']:.2f})")

    pay = data["payment"]
    print("\nPAYMENT")
    print("-" * 50)
    print(f"Method        : {pay['method']}")
    print(f"Card          : {pay['card']}")
    print(f"Approval Code : {pay['approval_code']}")
    print("=" * 50)


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "raw.txt")

    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)

    text = read_receipt(path)
    data = parse_receipt(text)

    # Human-readable report
    print_report(data)

    # Structured JSON output
    print("\nJSON OUTPUT")
    print("-" * 50)
    print(json.dumps(data, indent=2, ensure_ascii=False))

    # Save the JSON next to the receipt
    out_path = os.path.join(here, "receipt_parsed.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved structured output to {out_path}")


if __name__ == "__main__":
    main()
