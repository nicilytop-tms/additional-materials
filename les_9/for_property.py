class BankAccount:
    BONUS = 20

    def __init__(self, user_name, initial_deposit):
        self.name = user_name
        self.initial_deposit = initial_deposit
        self.amount = initial_deposit

    @property
    def money(self):
        return self.amount + BankAccount.BONUS if self.initial_deposit >= 30 else self.amount


peters_account = BankAccount('Peter', 45)
maxs_account = BankAccount('Max', 29)

print(peters_account.money)
print(peters_account.name)
print(maxs_account.money)
