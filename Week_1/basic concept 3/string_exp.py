name = 'Sourov\'s Mahmud' #escape character
name1 = "Sourov Mahmud"
name2 = """
    Sourov Mahmud
    Software Developer
"""

print(name1)
# string is a squence of characters
for char in name1:
    print(char)
print(name1[3]) #index accessing
print(name1[1:6]) #slicing
print(name1[-3:]) #negative indexing
print(name1[::-1]) #reversing a string

#find some of the portion of string
if 'Mahmud' in name1:
    print('Exist')
# sring is like list but immutable
# list is mutable, mutable means we can change the value
# string is immutable, immutable means we can not change the value