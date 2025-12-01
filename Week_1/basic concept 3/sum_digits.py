n = int(input())
ss = str(input())
sum = 0
for s in ss:
    sum += ord(s) - ord('0') # this is the way to convert char to digit
print(sum)
