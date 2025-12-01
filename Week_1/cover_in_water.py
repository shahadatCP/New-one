t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    cnt = 0
    yes = False
    
    for i in range(n):
        if s[i] == '.':
            cnt += 1
            if cnt >= 3:
                yes = True
        else:
            cnt = 0
    if yes:
        print(2)
    else:
        ans = 0
        for i in range(n):
            if s[i] == '.':
                ans += 1
        print(ans)