# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
    cart = [] # class attribute # static attribute
    origin = 'china'

    def __init__(self, name, location):
        self.name = 'Jamu na city' # instance attribute 
        self.location = 'Jam er maj khane'
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')
    
    @staticmethod
    def multiply(a, b):
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        print('hudai dekhi kintu kinmu na just ac er hawa khaite aschi', item)

# we don't have to pass an arguments for perchase() self in method
# if we stor Shopping to a instance like 'basundara'
basundara = Shopping('basu en dhara', 'not popular location')
basundara.purchase('lungi', 500, 1000)
#but here we have to pass an argument for self method, otherwise this will give us a error
# so we can't use  class directly without passing self arguments
Shopping.purchase('a', 2, 3 , 4)
# but we can do this by doing something call @classmethod
Shopping.hudai_dekhi('lungi')

Shopping.multiply(4, 5) # static method
# basundara.multiply(6,9) 