# lambda

# the real way to write a function
def doubled(x):
    return x*2
result = doubled(44)
print(result)

#the following code show us the use of lambda
doubled = lambda num : num*2 # this is the short way to write double function
squard = lambda num : num * num 
print(doubled(44), squard(9))

#multiple peramiter
add = lambda a,b  : a+b
print(add(11,33))

# lamda ft map
numbers = [12, 56, 98, 78, 56, 12, 6, 98]
doubble_nums = map(lambda x : x*2, numbers)
squared_nums = map(lambda x : x*x, numbers)
print(numbers)
print(list(doubble_nums))
print(list(squared_nums))

actors = [
    {'name' : 'sabana', 'age' : 65},
    {'name' : 'sabnoor', 'age' : 55},
    {'name' : 'sabila noor', 'age' : 38},
    {'name' : 'shaon', 'age' : 40},
    {'name' : 'srabonti', 'age' : 70},
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
Fivers = filter(lambda actor : actor['age']%5==0, actors)

# print(list(juniors))
print(list(Fivers))