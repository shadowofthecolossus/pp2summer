"""
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
"""
def myfunc():
      global x
      x = 300
myfunc()
print(x) 