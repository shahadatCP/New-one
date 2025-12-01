class Shop:
    shoppint_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # here cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


mina = Shop('mi na')
mina.add_to_cart('phone')
mina.add_to_cart('shoes')
print(mina.cart)

misu = Shop('mi su')
misu.add_to_cart('cap')
misu.add_to_cart('watch')
print(misu.cart)

apurvo = Shop('age purbo chilo')
apurvo.add_to_cart('chiruni')
print(apurvo.cart)