from decimal import Decimal


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.Decimal = Decimal
        self.Decimal = balance
        self.balance = Decimal

    def deposit(self, amount):
        if Decimal(amount < '0.00'):
            raise ValueError('Deposit amount must be positive.')
        self.balance += Decimal(amount)


david_account = Account("James Runner", Decimal('$345_981.71'))

print(david_account.name)
print(david_account.Decimal.values)
print(david_account.deposit('1000.00'))
