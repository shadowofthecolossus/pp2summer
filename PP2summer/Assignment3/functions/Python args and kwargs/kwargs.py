"""
The **kwargs parameter allows a function to accept any number of keyword arguments.
Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
"""
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen") 