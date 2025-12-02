class Watch:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_time(self):
        print('Displaying time...')

class FitnessTracker:
    def __init__(self, price):
        self.price = price
    
    def track_step(self):
        print('Tracking step')
    
    def track_calories(self):
        print('Tracking calories')

class SmartWatch(Watch, FitnessTracker):
    def __init__(self, brand, model, price):
        Watch.__init__(self,brand, model) # multple int.. er jonno self use korte hobe
        FitnessTracker.__init__(self, price) # same like previous line

apple_watch = SmartWatch('Apple', 'i8', 25000)
print(apple_watch.brand, apple_watch.model, apple_watch.price)