s = str(input())
cnt = 0
ss = []
ans = []
for char in s:
    if char == 'L':
        cnt += 1
        ss.append(char)
    elif char == 'R':
        cnt -= 1
        ss.append(char)
    if cnt == 0:
        ans.append(ss)
        ss = []
        
print(len(ans))
for sss in ans:
    print("".join(sss))

