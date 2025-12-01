# list, array, collection is same (simple terms)

# index =   0   1   2   3   4   5   6   7   8    9
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# index =  -10  -9  -8  -7  -6  -5  -4  -3  -2   -1

print(numbers[3], numbers[4], numbers[-6])
# so the key point is that positive index starts from left side and negative index starts from right side
# you can use both positive and negative index to access elements of list

# list (start:end) start index is inclusive and end index is exclusive
print(numbers[2:6])
print(numbers[1:7])

# list (start:end:step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1]) # this will give empty list because step is negative but start index is less than end index
print(numbers[7:2:-1]) # this will work because step is negative and start index is greater than end index
print(numbers[4:]) # this will give list from index 4 to end
print(numbers[:5]) # this will give list from start to index 4
print(numbers[:]) # this will give complete list and it's also called as shallow copy of list
print(numbers[::-1]) # this will give reversed list