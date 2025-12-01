n = int(input())
arr = list(map(int, input().split()))
cnt = 0
dic = {}
for num in arr:
    dic[num] = dic.get(num, 0) + 1
for key, value in dic.items():
    if value > key:
        cnt += value - key
    elif key > value:
        cnt += value
print(cnt)