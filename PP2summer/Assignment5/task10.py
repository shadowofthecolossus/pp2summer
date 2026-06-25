import re
with open("raw.txt", "r",encoding="utf-8") as f:
    text = f.read().strip()
print((r'(?<=[а-я])(?=[А-Я])', '_', text).lower())