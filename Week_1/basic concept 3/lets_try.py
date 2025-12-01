# this code didn't work out


n = int(input())
arr = list(map(int, input().split()))
cnt = 0
yes = 0
while True:
    for num in arr:
        if num % 2 == 0:
            num = num/2
        else:
            yes = 1
    if yes==0:
        cnt+=1
    else: 
        break
print(cnt)
