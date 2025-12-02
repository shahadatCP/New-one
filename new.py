class Phone:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def add_phone(self, name, price):
        self.name = name 
        self.price = price

phone1 = Phone('iphone', 52200)
print(phone1.name)
