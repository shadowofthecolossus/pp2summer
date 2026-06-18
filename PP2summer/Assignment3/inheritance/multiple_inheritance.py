class Flyer:
    def move(self) -> str:
        return "flies"


class Swimmer:
    def move(self) -> str:
        return "swims"


class Duck(Flyer, Swimmer):
    pass


class Duck2(Swimmer, Flyer):
    pass


def main():
    d1 = Duck()
    d2 = Duck2()

    print(d1.move())
    print(Duck.mro())

    print(d2.move())
    print(Duck2.mro())


if __name__ == "__main__":
    main()
