with open("tsk1", "a") as f:
  f.write(" bro")
with open("tsk1") as f:
  print(f.read())
f.close()