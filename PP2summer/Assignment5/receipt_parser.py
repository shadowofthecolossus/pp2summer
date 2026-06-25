import re
import json

with open('raw.txt', 'r', encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

# Parse products
products = []
i = 0
while i < len(lines):
    if re.match(r'^\d+\.$', lines[i].strip()):
        i += 1
        # Collect name (until we hit qty x price line)
        name_parts = []
        while i < len(lines) and not re.match(r'^\d[\d\s]*,\d+ x \d[\d\s]*,\d+$', lines[i].strip()):
            if lines[i].strip():
                name_parts.append(lines[i].strip())
            i += 1
        name = ' '.join(name_parts)
        # Parse "2,000 x 154,00"
        if i < len(lines):
            m = re.match(r'^([\d\s]+,\d+) x ([\d\s]+,\d+)$', lines[i].strip())
            if m:
                qty = float(m.group(1).replace(' ', '').replace(',', '.'))
                unit_price = float(m.group(2).replace(' ', '').replace(',', '.'))
                i += 1
                total = float(lines[i].strip().replace(' ', '').replace(',', '.'))
                products.append({
                    "name": name,
                    "quantity": qty,
                    "unit_price": unit_price,
                    "total": round(qty * unit_price, 2)
                })
    i += 1

text = '\n'.join(lines)

# Date/time
dt = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)

# Total
total_m = re.search(r'ИТОГО:\n([\d\s,]+)', text)
total = float(total_m.group(1).replace(' ', '').replace(',', '.')) if total_m else 0

# Payment
pay = re.search(r'(Банковская карта|Наличные):\n([\d\s,]+)', text)

result = {
    "store": {
        "name": re.search(r'Филиал (.+)', text).group(1).strip(),
        "bin": re.search(r'БИН (\d+)', text).group(1),
        "address": re.search(r'г\. .+', text).group(0).strip(),
        "date": dt.group(1) if dt else None,
        "time": dt.group(2) if dt else None
    },
    "receipt": {
        "number": re.search(r'Чек №(\d+)', text).group(1),
        "cashier": re.search(r'Кассир (.+)', text).group(1).strip()
    },
    "products": products,
    "summary": {
        "item_count": len(products),
        "calculated_total": round(sum(p["total"] for p in products), 2),
        "receipt_total": total
    },
    "payment": {
        "method": pay.group(1) if pay else "Unknown",
        "amount": float(pay.group(2).replace(' ', '').replace(',', '.')) if pay else 0
    },
    "vat_12_percent": 0.0
}

print(json.dumps(result, ensure_ascii=False, indent=2))