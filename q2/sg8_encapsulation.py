class BankAccount:
    def __init__(self, account_num: int, initial_balance: float):
        self.update_account_number(account_num)
        self.update_balance(initial_balance)

        print("Account 1")
        print(f"Account Number: {self.__account_num}")
        print(f"Balance: {self.__balance:.2f}")

    def update_account_number(self, number: int):
        self.__account_num = int(number)

    def update_balance(self, amount: float):
        print(f"Update balance to {amount}")

        if amount < 0:
            print("The balance must not be a negative number.")
            return

        self.__balance = float(amount)

    def set_account_number(self, number: int):
        self.update_account_number(number)

    def set_balance(self, amount: float):
        self.update_balance(amount)

    @property
    def account_number(self):
        return self.__account_num

    @property
    def balance(self):
        return self.__balance

xi = BankAccount(21011, 1975)
xi.set_balance(1600)
xi.set_balance(-1600)

print("Account 1")
print(f"Account Number: {xi.account_number}")
print(f"Balance: {xi.balance:.2f}")
