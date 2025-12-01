# poly --> many (multiple)
# morph -- > shape
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    # if we do not write the bellwo code than ouput will show us the parent class print
    # but after writing this, now this will print
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('ghew ghew')
class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('suii suii')


don = Cat('Real don')
don.make_sound()

shepard = Dog('Local shephard')
shepard.make_sound()

cr = Goat('Cristano Ronaldo')
cr.make_sound()

less = Goat('gora gori')

animals = [don, shepard, cr, less]

for animal in animals:
    animal.make_sound()