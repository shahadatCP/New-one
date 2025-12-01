numbers = [12, 56, 98, 78, 56, 12, 26, 98]
person = ['Kala Chan', 'Kalipur', 23, 'student']
#key value pair
#dictionary
#object
#hash table
#overlap with set

#{key : value, key : value}
person = {'name':'Kala Pakhi', 'address': 'kalipur', 'age':23, 'job':'baker'}
print(person)
#we can access specific thing like bellow
print(person['job'])
print(person.keys())
print(person.values())
#we can add new key value
person['language'] = 'python'\
#we can change the keys value
person['job'] = 'cd'
#we can delet keys value
del person['age']
print(person)

#run loop for dictionary

#if we run loop like this, it will only give us the keys
for item in person:
    print(item)
#for real loop we have to write f like this
for key, value in person.items():
    print(key, value) 