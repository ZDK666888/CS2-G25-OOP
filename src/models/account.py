from datetime import datetime

from src.exceptions import InsufficientFundsError, InvalidAmountError
from src.models.base import BaseRecord


class Account(BaseRecord):
    def __init__(
        self,
        account_id,
        name,
        account_type,
        balance=0,
        currency="USD",
    ):
        if balance < 0:
            raise InvalidAmountError("Balance cannot be negative")

        super().__init__(record_id=account_id)
        self.account_id = account_id
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self._validate_positive_amount(amount)
        self.balance += amount
        self.touch()

    def withdraw(self, amount):
        self._validate_positive_amount(amount)
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")

        self.balance -= amount
        self.touch()

    def rename(self, new_name):
        self.name = new_name
        self.touch()

    def to_dict(self):
        data = super().to_dict()
        data.update(
            {
                "account_id": self.account_id,
                "name": self.name,
                "account_type": self.account_type,
                "balance": self.balance,
                "currency": self.currency,
            }
        )
        return data

    @classmethod
    def from_dict(cls, data):
        account = cls(
            account_id=data.get("account_id", data.get("id")),
            name=data["name"],
            account_type=data["account_type"],
            balance=data["balance"],
            currency=data["currency"],
        )
        account.created_at = datetime.fromisoformat(data["created_at"])
        account.updated_at = datetime.fromisoformat(data["updated_at"])
        return account

    def _validate_positive_amount(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
