class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} meows"


def main():
    a = Animal("Creature")
    d = Dog("Rex")
    c = Cat("Milo")

    print(a.speak())
    print(d.speak())
    print(c.speak())

    print(isinstance(d, Animal))
    print(isinstance(a, Dog))


if __name__ == "__main__":
    main()
