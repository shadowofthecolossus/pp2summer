class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self) -> str:
        return f"{self.owner}: {self.balance:.2f}"


class FeeAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, fee: float = 1.0):
        super().__init__(owner, balance)
        self.fee = float(fee)

    def withdraw(self, amount: float) -> None:
        total = amount + self.fee
        super().withdraw(total)


def main():
    a = BankAccount("Dana", 50)
    f = FeeAccount("Tim", 50, fee=2)

    print(a)
    a.withdraw(10)
    print(a)

    print(f)
    f.withdraw(10)
    print(f)

    try:
        f.withdraw(100)
    except ValueError as e:
        print(type(e).__name__, str(e))


if __name__ == "__main__":
    main()
