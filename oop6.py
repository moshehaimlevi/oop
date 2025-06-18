from abc import ABC, abstractmethod
from typing import Optional, Dict


class ITransfer(ABC):
    @abstractmethod
    def transfer(self, amount: float, to_account: 'BankAccount') -> bool:
        pass


class IVerifyCreditCard(ABC):
    @abstractmethod
    def verify_credit_card(self, card_number: str) -> bool:
        pass


class IVerifyPayPal(ABC):
    @abstractmethod
    def verify_paypal_email(self, email: str) -> bool:
        pass



class BankAccount(ITransfer, IVerifyCreditCard, IVerifyPayPal):
    def __init__(self, id: str, balance: float, credit_card_number: Optional[str] = None, paypal_email: Optional[str] = None):
        self.id = id
        self.balance = balance
        self.credit_card_number = credit_card_number
        self.paypal_email = paypal_email

    def transfer(self, amount: float, to_account: 'BankAccount') -> bool:
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            print(f"Transferred ${amount:.2f} from {self.id} to {to_account.id}")
            return True
        else:
            print(f"Transfer failed: Insufficient funds in account {self.id}")
            return False

    def verify_credit_card(self, card_number: str) -> bool:
        return self.credit_card_number == card_number

    def verify_paypal_email(self, email: str) -> bool:
        return self.paypal_email == email

    def __str__(self):
        return f"BankAccount(id={self.id}, balance={self.balance:.2f})"



class Payment(ABC):
    def __init__(self, amount: float, from_account_id: str, to_account_id: str):
        self.amount = amount
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id

    @abstractmethod
    def process(self, accounts: Dict[str, BankAccount]) -> bool:
        pass



class CreditCardPayment(Payment):
    def __init__(self, amount: float, from_account_id: str, to_account_id: str, card_number: str):
        super().__init__(amount, from_account_id, to_account_id)
        self.card_number = card_number

    def process(self, accounts: Dict[str, BankAccount]) -> bool:
        from_account = accounts.get(self.from_account_id)
        to_account = accounts.get(self.to_account_id)

        if not isinstance(from_account, IVerifyCreditCard):
            print("Source account does not support credit card verification.")
            return False

        if not from_account.verify_credit_card(self.card_number):
            print(f"Credit card verification failed for account {self.from_account_id}.")
            return False

        return from_account.transfer(self.amount, to_account)



class PayPalPayment(Payment):
    def __init__(self, amount: float, from_account_id: str, to_account_id: str, email: str):
        super().__init__(amount, from_account_id, to_account_id)
        self.email = email

    def process(self, accounts: Dict[str, BankAccount]) -> bool:
        from_account = accounts.get(self.from_account_id)
        to_account = accounts.get(self.to_account_id)

        if not isinstance(from_account, IVerifyPayPal):
            print("Source account does not support PayPal verification.")
            return False

        if not from_account.verify_paypal_email(self.email):
            print(f"PayPal verification failed for account {self.from_account_id}.")
            return False

        return from_account.transfer(self.amount, to_account)



def main():
    accounts = {
        "A001": BankAccount("A001", 1000.0, credit_card_number="1234567890123456", paypal_email="user1@example.com"),
        "A002": BankAccount("A002", 500.0, credit_card_number="1111222233334444", paypal_email="user2@example.com")
    }

    payments = [
        CreditCardPayment(200.0, "A001", "A002", card_number="1234567890123456"),  # Valid
        PayPalPayment(300.0, "A001", "A002", email="wrong@example.com"),           # Invalid email
        CreditCardPayment(900.0, "A002", "A001", card_number="1111222233334444")   # Insufficient funds
    ]

    for payment in payments:
        result = payment.process(accounts)
        print(f"Payment result: {result}")
        print("-" * 40)

    for acc in accounts.values():
        print(acc)

if __name__ == "__main__":
    main()