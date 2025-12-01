import random
# ans = random.randint(70, 100)
class Exam:

    def __init__(self, sub):
        self.sub = sub
               
    
    def is_prestnt(self, num):
        if num == 1:
            ans = random.randint(70, 100)
            print(f'you got the {ans} in the examinaton')

        elif num == 0:
            print('you didn\'t got the mark')
        else:
            print('Invalid')

mahi = Exam('math')
mahi.is_prestnt(1)

rafi = Exam('bangla')
rafi.is_prestnt(1)