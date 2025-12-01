numbers = [12, 45, 98, 68]
numbers.append(100)  # adds 100 at the end of the list
print(numbers)
numbers.insert(2, 77) # adds 77 at index 2 but shifts rest of the elements to right
print(numbers)
if 45 in numbers:
    numbers.remove(45) # removes first occurrence of 45 from the list
if 200 in numbers:
    numbers.remove(200) # this will give error because 200 is not in the list but never effect your code
print(numbers)
last = numbers.pop() # removes and returns last element of the list
print(last, numbers)
last = numbers.pop(-2) #removes and returns element at index -2
print(last, numbers)

index = numbers.index(12) # returns index of first occurrence of 12 in the list
print(index)

index = numbers.index(68) # returns index of first occurrence of 68 in the list
print(index)

if 77 in numbers:
    index = numbers.index(77)
    print(index)
numbers.sort()
print(numbers) # prints sorted list
sorted = numbers.sort() # sorts the list in ascending order
print(sorted) # prints None because sort() method doesn't return anything
print(numbers) # prints sorted list 

numbers.reverse()
print(numbers) # prints reversed list