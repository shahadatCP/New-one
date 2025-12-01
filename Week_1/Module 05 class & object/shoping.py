class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
    
    
    #remove from cart[]
    def remove_item(self):
        string = input('Enter the name of the item to remove: ')
        for item in self.cart:
            if item['item'] == string:
                self.cart.remove(item)
                break
            
        else:
            print('Item not found in cart. Nothing removed')



    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money: {extra}')

rafi = Shopping('rafi hasan')
rafi.add_to_cart('alu', 50, 6)
rafi.add_to_cart('dim', 12, 24)
rafi.add_to_cart('rice', 50, 5)


print(rafi.cart)
rafi.checkout(1200)
rafi.remove_item()
print(rafi.cart)

rafi.checkout(1200)
