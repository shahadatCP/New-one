# inheritance provides you "is a" relation
class Animal:
    pass

# Dog is a animal
class Dog(Animal):
    pass

# Tiger is a animal
class Tiger(Animal):
    pass

class Engine:
    def __init__(self):
        pass
    def start(self):
        return 'Engin started'
class Driver:
    def __init__(self):
        pass

# car 'has a' engin
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()  