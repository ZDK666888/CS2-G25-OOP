import pytest

from src.exceptions import InsufficientFundsError, InvalidAmountError
from src.models.account import Account
from src.models.base import BaseRecord


def test_create_account():
    account = Account(
        account_id="acc-1",
        name="Cash Wallet",
        account_type="cash",
        balance=100,
        currency="USD",
    )

    assert account.id == "acc-1"
    assert account.account_id == "acc-1"
    assert account.name == "Cash Wallet"
    assert account.account_type == "cash"
    assert account.balance == 100
    assert account.currency == "USD"


def test_account_inherits_base_record():
    account = Account("acc-1", "Cash Wallet", "cash")

    assert isinstance(account, BaseRecord)
    assert account.created_at == account.updated_at


def test_deposit_increases_balance_and_updates_timestamp():
    account = Account("acc-1", "Cash Wallet", "cash", balance=100)
    old_updated_at = account.updated_at

    account.deposit(50)

    assert account.balance == 150
    assert account.updated_at > old_updated_at


def test_withdraw_decreases_balance_and_updates_timestamp():
    account = Account("acc-1", "Cash Wallet", "cash", balance=100)
    old_updated_at = account.updated_at

    account.withdraw(40)

    assert account.balance == 60
    assert account.updated_at > old_updated_at


@pytest.mark.parametrize("amount", [0, -1])
def test_deposit_rejects_invalid_amount(amount):
    account = Account("acc-1", "Cash Wallet", "cash", balance=100)

    with pytest.raises(InvalidAmountError):
        account.deposit(amount)


@pytest.mark.parametrize("amount", [0, -1])
def test_withdraw_rejects_invalid_amount(amount):
    account = Account("acc-1", "Cash Wallet", "cash", balance=100)

    with pytest.raises(InvalidAmountError):
        account.withdraw(amount)


def test_create_account_rejects_negative_balance():
    with pytest.raises(InvalidAmountError):
        Account("acc-1", "Cash Wallet", "cash", balance=-1)


def test_withdraw_rejects_insufficient_funds():
    account = Account("acc-1", "Cash Wallet", "cash", balance=100)

    with pytest.raises(InsufficientFundsError):
        account.withdraw(101)


def test_rename_updates_name_and_timestamp():
    account = Account("acc-1", "Cash Wallet", "cash")
    old_updated_at = account.updated_at

    account.rename("Daily Cash")

    assert account.name == "Daily Cash"
    assert account.updated_at > old_updated_at


def test_to_dict_returns_account_fields():
    account = Account(
        account_id="acc-1",
        name="Cash Wallet",
        account_type="cash",
        balance=100,
        currency="USD",
    )

    result = account.to_dict()

    assert result == {
        "id": "acc-1",
        "created_at": account.created_at.isoformat(),
        "updated_at": account.updated_at.isoformat(),
        "account_id": "acc-1",
        "name": "Cash Wallet",
        "account_type": "cash",
        "balance": 100,
        "currency": "USD",
    }


def test_from_dict_restores_account():
    original = Account(
        account_id="acc-1",
        name="Cash Wallet",
        account_type="cash",
        balance=100,
        currency="USD",
    )
    restored = Account.from_dict(original.to_dict())

    assert restored.id == original.id
    assert restored.account_id == original.account_id
    assert restored.name == original.name
    assert restored.account_type == original.account_type
    assert restored.balance == original.balance
    assert restored.currency == original.currency
    assert restored.created_at == original.created_at
    assert restored.updated_at == original.updated_at
