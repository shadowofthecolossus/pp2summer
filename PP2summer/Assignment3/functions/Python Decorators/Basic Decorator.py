
"""
Decorators let you add extra behavior to a function, without changing the function's code.
A decorator is a function that takes another function as input and returns a new function.
"""
#Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
    def myinner():
        return func().upper()
        return myinner
@changecase
def myfunction():
    return "Hello Sally"
print(myfunction())