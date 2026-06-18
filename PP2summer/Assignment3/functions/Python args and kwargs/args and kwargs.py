"""
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.
"""
#Using *args to accept any number of arguments:

def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") 