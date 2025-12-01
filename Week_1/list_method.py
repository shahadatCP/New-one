numbers = [12, 45, 98, 64]

numbers.append(56)
# print(numbers)
numbers.insert(0,34)
# print(numbers)
numbers.insert(2,77)
# print(numbers)
numbers.remove(98)
# print(numbers)
if 100 in numbers:
    numbers.remove(100)
print(numbers)

last = numbers.pop()
print(last, numbers)
if 21 in numbers:
    index = numbers.index(21)
    print(index)
sorted_numbers = numbers.sort()
print(sorted_numbers) #this will print None because sort() method sorts the list in place and returns None
numbers.sort()
print(numbers)