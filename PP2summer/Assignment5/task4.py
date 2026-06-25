import re
with open("raw.txt", "r",encoding="utf-8") as f:
    text = f.read().strip()
if re.findall(r'[А-Я][а-я]+', text):
    print("match")
else:
    print("no")