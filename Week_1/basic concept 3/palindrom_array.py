num = int(input())
arr = list(map(str, input()))
arr2 = list(map(str, reversed(arr)))

# print(arr, arr2)

if arr == arr2:
    print('YES')
else: print('NO')

