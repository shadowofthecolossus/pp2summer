import re
with open("raw.txt", "r",encoding="utf-8") as f:
    text = f.read().strip()
print(re.split(r'(?=[А-Я])', text)) 