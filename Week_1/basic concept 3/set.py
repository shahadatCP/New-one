#list --> []
#tuple --> ()
#set --> {}
#set: unique collection of items
numbers = [12,56,98,78,56,12,6,98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set) #duplicates are removed
numbers_set.add(100)
print(numbers_set)
numbers_set.remove(56)
print(numbers_set)

for item in numbers_set:
    print(item)
if 44 in numbers_set:
    print('exists')
elif 100 in numbers_set:
    print('found 100')

a = {1, 3, 5, 7}
b = {1, 2, 3, 4, 5}
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)
#the first and second print line are same, they show union of two sets
#the third and fourth print line are same, they show intersection of two sets

