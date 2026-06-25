import re
with open("raw.txt", "r",encoding="utf-8") as f:
    text = f.read().strip()
if re.search(r"а.*б$",text):
    print("match")
else:
    print("no")