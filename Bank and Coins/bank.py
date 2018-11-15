class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds to withdraw £{}!".format(amount))

    def statement(self):
        print("Account Balance: £{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{} owns £ {} in the Current Account ".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{} owns £ {} in the Savings Account ".format(self.name, self.balance)


print("Current Account:")
current_account = Current("Karthik", 500)
current_account.deposit(1000)
current_account.statement()
current_account.withdraw(200)
current_account.statement()
current_account.withdraw(2400)
current_account.statement()

print()
print("Savings Account:")
savings_account = Savings("Karthik", 500)
savings_account.deposit(100)
savings_account.statement()
savings_account.withdraw(200)
savings_account.statement()
savings_account.withdraw(401)
savings_account.statement()