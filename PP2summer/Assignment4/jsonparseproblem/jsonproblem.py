import json
with open("sample-data.json", "r") as s:
    data = json.load(s)
print("Interface Status\n================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------")
for item in data["imdata"]:
    a = item["l1PhysIf"]["attributes"]
    print(a["dn"] + " " * 10 + a["descr"] + " " * 20 + a["speed"] + " " * 7 + a["mtu"])