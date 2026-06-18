"""
When you call a function with arguments without using keywords, they are called positional arguments.
Positional arguments must be in the correct order:
"""
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function("dog", "Buddy") 
