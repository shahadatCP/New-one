# for _ in range(int(input())):
#     n = int(input())
#     if 360 % (180 - n) == 0:
#         print('YES')
#     else:
#         print('NO')
# the above code is oky but we're trying in different
t = int(input())
for _ in range(t):
    n = int(input())
    if 360 % (180-n) == 0:
        print('YES')
    else:
        print('NO')

# now both code are oky