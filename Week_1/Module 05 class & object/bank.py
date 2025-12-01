class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Your balance after deposit {self.balance}')

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You can\'t withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You can\'t withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'your balance after withdraw {self.get_balance()}')
        
sonali = Bank(25000)
sonali.withdraw(25)
sonali.withdraw(5000000)
sonali.deposit(12000)
sonali.withdraw(12222)


nrbc = Bank(5000)
nrbc.deposit(2000)
nrbc.deposit(2000)
print(nrbc.get_balance())
        