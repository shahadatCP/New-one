name = 'sourov mahmud'
txt = 'HELLO WORLD'
#capitalize only the first letter of the string
c_name = name.capitalize()
print(c_name)

print(name.upper()) #convert all letters to uppercase
print(txt.lower()) #convert all letters to lowercase
print(name.title()) #convert first letter of each word to uppercase
print(txt.swapcase()) #swap the case of each letter
print(name.count('o')) #count the number of occurrences of a substring
print(name) #original string remains unchanged

#capitalize() method
s = 'hello WORLD'
print(s.capitalize()) #captalize only the first letter of the string

#lower() method
stt = 'GOODLUCK'
stt2 = '&'
print(stt.lower(), stt2.lower())

#casefold() method
string = 'GEEKSFORGEEKS'
string2 = 'ß'
print(string.casefold(), string2.casefold())

#the difference between lower() and casefold() is that casefold() is more aggressive in converting characters to lowercase, making it suitable for caseless matching, especially in certain languages.
