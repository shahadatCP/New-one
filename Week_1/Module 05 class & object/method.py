# def call():
#     print('calling someone I don\'t know')
#     return 'call'

class Phone:
    price = 12000
    color = 'black'
    brand = 'honor'
    features = ['camera', 'speaker', 'radio']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending SMS to : {phone} and messege: {sms}'
        return text
    

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4151, 'I miss you')
print(result)