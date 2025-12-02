class Shop:
    # products = [] # this is class attribute

    def __init__(self, name):
        self.name = name
        self.products = [] # this is instance attribute
        self.__balance = 500 # private attribute

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)
    
    def get_balance(self):
        return self.__balance

    def __str__(self): # this is called dander method 
        return f'This is a shop with name {self.name}'
    
    # def __repr__(self): # this is also a dander method but every time object first look for __str__ is he don't find that than he will came here for work
    #     return f'This is a shop name {self.name}'
        
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # def __str__(self):
    #     return self.name

    def __repr__(self):
        return self.name


shop1 = Shop('test shop 1')
shop1.add_product('Mobile', 20000)
shop1.add_product('Laptop', 100000)

# print(shop1.products)

shop2 = Shop('Test Shop 2')
shop2.add_product('Monitor', 20000)
shop2.add_product('Keyboard', 1000)

print(shop1.get_balance())


"""
Brac Bank [class attribute]
- Dhaka Brance
- Rajshahi Branch [instance attribute]
"""

"""
Access Modifier
- Public
- Private 
- Protected
"""