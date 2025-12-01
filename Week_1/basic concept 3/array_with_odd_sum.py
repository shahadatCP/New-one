t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    even = 0; odd = 0; sum = 0
    for num in arr:
        if num % 2 == 0:
            even+=1
        else:
            odd+=1
        sum += num
    if sum % 2 == 1: 
        print('YES')
    elif odd > 0 and even > 0:
        print('YES')
    else:
        print('NO')