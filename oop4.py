

class BankAccount:
    __bank_address = "1 Allenby St, Tel Aviv"

    def __init__(self, owner: str, balance: float):
        self._owner = owner
        self._balance = float(balance)


    @classmethod
    def get_bank_address(cls) -> str:
        return cls.__bank_address


    @staticmethod
    def highest_balance(acc1, acc2, acc3) -> float:
        return max(acc1.balance, acc2.balance, acc3.balance)


    @property
    def owner(self):
        return self._owner  # Read-only

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = float(value)


    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._balance -= amount

    def is_rich(self) -> bool:
        return self._balance > 1_000_000


    def __add__(self, other):
        if isinstance(other, BankAccount):
            if self.owner == other.owner:
                return BankAccount(self.owner, self.balance + other.balance)
            else:
                return f"Joint: {self.owner} & {other.owner}"
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.owner, self.balance - other.balance)
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance - other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.balance == other.balance
        elif isinstance(other, (int, float)):
            return self.balance == other
        elif isinstance(other, tuple) and len(other) == 2:
            return self.owner == other[0] and self.balance == other[1]
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.balance > (other.balance if isinstance(other, BankAccount) else other)

    def __ge__(self, other):
        return self.balance >= (other.balance if isinstance(other, BankAccount) else other)

    def __lt__(self, other):
        return self.balance < (other.balance if isinstance(other, BankAccount) else other)

    def __le__(self, other):
        return self.balance <= (other.balance if isinstance(other, BankAccount) else other)

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"

    def __len__(self):
        return round(self.balance)

    def __getitem__(self, key):
        if key == "owner" or key == 0:
            return self.owner
        elif key == "balance" or key == 1:
            return self.balance
        else:
            raise KeyError("Invalid key. Use 'owner', 'balance', 0 or 1")

    def __iter__(self):
        yield self.owner
        yield self.balance



###################### DEMO CODE ######################
acc1 = BankAccount("Alice", 800.0)
acc2 = BankAccount("Bob", 1200.0)
acc3 = BankAccount("Alice", 800.0)
acc4 = BankAccount("Charlie", 300.0)


print("Accounts:")
print(acc1)
print(acc2)
print(acc3)


print("\nEquality:")
print("acc1 == acc3:", acc1 == acc3)
print("acc1 == acc2:", acc1 == acc2)
print("acc1 == 800:", acc1 == 800)
print("acc1 == ('Alice', 800):", acc1 == ("Alice", 800))  # True


print("\nInequality:")
print("acc1 != acc2:", acc1 != acc2)


print("\nGreater Than:")
print("acc2 > acc1:", acc2 > acc1)
print("acc4 > acc1:", acc4 > acc1)


print("\nOther comparisons:")
print("acc1 < acc2:", acc1 < acc2)
print("acc2 >= acc1:", acc2 >= acc1)
print("acc4 <= acc1:", acc4 <= acc1)


print("\nAdd:")
acc5 = acc1 + acc3
print("acc5 (Alice + Alice):", acc5)


acc6 = acc1 + acc2
print("acc6 (Alice + Bob):", acc6)


acc7 = acc1 + 200
print("acc1 + 200:", acc7)


acc8 = acc2 - acc1
print("acc2 - acc1:", acc8)


acc9 = acc2 - 500
print("acc2 - 500:", acc9)


print("\nGet item:")
print("acc1['owner']:", acc1['owner'])
print("acc1[1]:", acc1[1])

print("\nIterating acc1:")
for info in acc1:
    print(info)


print("\nLength of acc1:", len(acc1))

print("\nBank address:", BankAccount.get_bank_address())

print("\nHighest balance:", BankAccount.highest_balance(acc1, acc2, acc4))






