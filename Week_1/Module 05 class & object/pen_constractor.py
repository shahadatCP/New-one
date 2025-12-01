class Pen:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

matador_pen = Pen('Matador', 'Red', 5)
print(matador_pen.name, matador_pen.color, matador_pen.price)

goodluck_pen = Pen('Good Luck', 'Black', 5)
print(goodluck_pen.name, goodluck_pen.color, goodluck_pen.price)

alltime_pen = Pen('All Time', 'Yeollow', 7)
print(alltime_pen.name, alltime_pen.color, alltime_pen.price)
