class Shop:
    cart = [] # here this cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)

mina = Shop('Mi na')
mina.add_to_cart('shoes')
mina.add_to_cart('phone')
print(mina.cart)

nisa = Shop('nisa')
nisa.add_to_cart('cap')
nisa.add_to_cart('watch')

print(nisa.cart)