class Vehicale:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicale):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

class Bike(Vehicale):
    def __init__(self, brand, model, milage):
        super().__init__(brand, model)
        self.milage = milage

bmw = Car('BMW', 'V3', 7)
print(bmw.brand, bmw.model, bmw.capacity)
suzuki = Bike('Suzuki', 's3', 48)
print(suzuki.brand, suzuki.model, suzuki.milage)