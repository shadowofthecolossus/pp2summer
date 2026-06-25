import re
with open("raw.txt", "r",encoding="utf-8") as f:
    text = f.read().strip()
if re.findall(r'[а-я]+_[а-я]+', text):
    print("match")
else:
    print("no")