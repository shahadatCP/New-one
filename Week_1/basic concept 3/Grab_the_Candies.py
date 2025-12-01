t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # for num in arr:
    #   print(num)
    #  print(arr)
        
    even = 0
    odd = 0
    for num in arr:
        if num % 2 == 0:
            even += num
        else: 
            odd += num
    if even > odd:
        print('Yes')
    else:
        print('No')