n = int(input())
arr = list(map(int, input().split()))
cnt = 0
yes = 0
while True:
    for i in range(len(arr)):
        if(arr[i]%2==0):
            arr[i] = arr[i]/2
        else:
            yes = 1
    if yes==0:
        cnt+=1
    else: 
        break
print(cnt)