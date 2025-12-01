chars = input()
copy_char = []
for char in chars[::-1]:
    if not copy_char and char == '0':
        continue
    copy_char.append(char)
copy_char_str = ''.join(copy_char)
if chars == copy_char_str:
    print(copy_char_str)
    print("YES")
else:
    print(copy_char_str)
    print("NO")
