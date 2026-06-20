# json_handling.py
# Parsing and creating JSON
#
# NOTE: this file is named json_handling.py on purpose, NOT json.py.
# Naming it json.py would clash with Python's built-in json module
# and break the "import json" line below.

import json

# ---------- PYTHON OBJECT -> JSON STRING (json.dumps) ----------
person = {
    "name": "Aisha",
    "age": 21,
    "city": "Taraz",
    "is_student": True,
    "courses": ["Python", "Discrete Structures"]
}

json_string = json.dumps(person)
print("JSON string:", json_string)

# indent makes it readable; sort_keys orders the keys
pretty = json.dumps(person, indent=4, sort_keys=True)
print("Pretty JSON:")
print(pretty)


# ---------- JSON STRING -> PYTHON OBJECT (json.loads) ----------
raw = '{"product": "Sponge", "price": 890, "available": true}'
data = json.loads(raw)
print("Parsed dict:", data)
print("Price field:", data["price"])      # access like a normal dict
print("Available?", data["available"])     # JSON true -> Python True


# ---------- WRITING JSON TO A FILE (json.dump) ----------
output = {
    "store": "The Glory",
    "items_sold": 42,
    "best_seller": "Silicone Toilet Brush"
}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4, ensure_ascii=False)
print("Saved output.json")


# ---------- READING JSON FROM A FILE (json.load) ----------
# Reading the sample-data.json that ships with this practice
with open("sample-data.json", "r", encoding="utf-8") as f:
    store_data = json.load(f)

print("Store name:", store_data["store"])
print("Total products:", store_data["total_products"])

# Working with the loaded data
print("Products in stock:")
for product in store_data["products"]:
    if product["in_stock"]:
        print(f"  - {product['name']}: {product['price']} {product['currency']}")

# Calculate total value of in-stock items
total_value = sum(
    p["price"] for p in store_data["products"] if p["in_stock"]
)
print("Total value of in-stock products:", total_value, "KZT")
