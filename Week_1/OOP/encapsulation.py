# encapsulation --> hide details
# access modifier: public, protected, privet
class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name # this is public we can access this from anywhere and we can change is
        self._branch = 'banani 11'
        # self.balance = initial_deposit
        self.__balance = initial_deposit # this is privet we can't access form outside 
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'Taka nai'

    def __repr__(self):
        return f'Our castomar {self.holder_name} has {self.__balance} in his bank account'

rafsan = Bank('Choto vai', 10000)
# print(rafsan)
print(rafsan.holder_name)
rafsan.deposit(50000)
print(rafsan)
print(rafsan._branch)
rafsan.withdraw(20000)
print(rafsan)
print(dir(rafsan)) # this help us to find the next line name in all
print(rafsan._Bank__balance) # chipa diye check hahaha