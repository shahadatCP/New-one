l,r = map(int, input().split())
myfault = False
for num in range(l,r+1):
    s = str(num)
    bool = True
    for ch in s:
        if ch == '4' or ch == '7':
            continue
        else:
            bool = False
    if bool:
        myfault = True
        print(num, end=' ')
if not myfault:
    print(-1)