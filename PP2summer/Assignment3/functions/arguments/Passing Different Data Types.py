"""
You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

The data type will be preserved inside the function:
"""
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) 