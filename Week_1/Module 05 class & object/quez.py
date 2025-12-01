# def call():
#     print('calling someone I do not know')
#     return 'call done'
# class Phone:
#     p = 1200
#     c = 'blue'
#     b = 'honor'
#     fe = ['camere', 'speaker', 'hammer']
    
#     def call(self):
#         print('calling someone i konw')

# my_phone = Phone()
# call()

# class A:
#     def __init__(self, value):
#         value = 3
#         self.value = value
#     def change(self):
#         self.value = 12
# ans = []
# a = A(13)
# ans.append(a.value)
# a.change()
# ans.append(a.value)
# print(ans)


# class Shop:
#     cart = []

#     def __init__(self,buyer):
#         self.buyer = buyer

#     def add_to_cart(self, item):
#         self.cart.append(item)

# p1 = Shop('he')
# p1.add_to_cart('shoes')
# p1.add_to_cart('phone')

# niso = Shop('niso')
# niso.add_to_cart('cap')
# niso.add_to_cart('watch')
# print(niso.cart)


class Phone:
    p = 12
    c = 'r'
    b = 's'

    def call(self):
        print('callint one person')
    
    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone + 5}'
        return text
my_phone = Phone()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)
