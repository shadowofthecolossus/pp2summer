"""
You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments:
"""
def my_function(name, /):
      print("Hello", name)
my_function("Emil") 