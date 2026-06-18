#Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:
def changecase(func):
      def myinner(x):
            return func(x).upper()
      return myinner
@changecase
def myfunction(nam):
  return "Hello " + nam
print(myfunction("John"))