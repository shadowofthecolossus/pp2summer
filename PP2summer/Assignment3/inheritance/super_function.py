class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def info(self) -> str:
        return f"{self.name}, {self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, school: str):
        super().__init__(name, age)
        self.school = school

    def info(self) -> str:
        base = super().info()
        return f"{base}, {self.school}"


def main():
    p = Person("Amina", 30)
    s = Student("Arman", 16, "High School")

    print(p.info())
    print(s.info())


if __name__ == "__main__":
    main()
