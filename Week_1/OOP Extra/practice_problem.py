class Product:
    def __init__(self, name, origin, price):
        self.name = name
        self.origin = origin
        self.price = price

class Shop:
    def __init__(self):
            self.products = []

    def add_product(self, product):
        self.products.append(product)

    def buy_product(self, name, price):
         for product in self.products:
                if product.name == name:
                   if price < product.price:
                        print(f'You have to pay {product.price - price} TK more')
                        return
                   else:
                        print(f'Congratulations! You bought the product. Here is your change {price - product.price}')
                        self.products.remove(product)
                        return 
         
         print('Not available')              

my_shop = Shop()

my_shop.add_product(Product('Laptop', 'usa', 1000))
my_shop.add_product(Product('Phone', 'china', 1200))
my_shop.add_product(Product('watch', 'BD', 500))

my_shop.buy_product('Phone', 1999)  
my_shop.buy_product('Phone', 899) 
my_shop.buy_product('tablet', 1545)