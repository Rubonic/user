class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02,0)

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.balance += amount	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self,amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f'{self.name} ${self.account.balance}')
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self


class BankAccount:
    all_accounts = []

    def __init__(self,int_rate,balance):
        self.balance = 0
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def print_all_balances(cls):
        for account in cls.all_accounts:
            print(f'Balance: ${account.balance}')

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: Chargin a $5 fee')
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate*self.balance
        return self


John = BankAccount(0.02, 3000)
Terry = BankAccount(0.03, 10000)

John.deposit(500).deposit(1000).deposit(500).yield_interest().display_account_info()
Terry.deposit(600).deposit(300).withdraw(1000).withdraw(1000).withdraw(300).withdraw(1000).yield_interest().display_account_info()
        
BankAccount.print_all_balances()


    # def all_balances(cls):
    #     sum = 0
    #     # we use cls to refer to the class
    #     for account in cls.all_accounts:
    #         sum += account.balance
    #     return sum




guido = User("Guido Van Rossum", "guido@dojo.com")
monty = User("Monty Python", "monty@python.com")
logan = User("Logan Domingo", "logankdoming@dojo.com")

guido.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawal(150).display_user_balance()

monty.make_deposit(500).make_deposit(200).make_withdrawal(100).make_withdrawal(300).display_user_balance()

logan.make_deposit(1000).make_withdrawal(500).make_withdrawal(200).make_withdrawal(300).display_user_balance()

guido.transfer_money(logan, 300)

guido.display_user_balance()
logan.display_user_balance()




