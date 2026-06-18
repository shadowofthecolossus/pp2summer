#A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
def changecase(func):
      def myinner():
            return func().upper()
      return myinner
@changecase
def myfunction():
  return "Hello Sally"
@changecase
def otherfunction():
    return "I am speed!"
print(myfunction())
print(otherfunction())