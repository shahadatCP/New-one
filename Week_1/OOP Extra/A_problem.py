class Bank:
    bank_name = 'ABC Bank'
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
    
    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.balance += amount
            print(f'Deposited {amount}. New balance: {self.balance}')
        else:
            print('Invalid amount')

acc = Bank('Sourov', 1000)

acc.deposit(500)
acc.deposit(-500)

print(acc.bank_name)
acc.change_bank_name('XYZ Bank')
print(acc.bank_name)
