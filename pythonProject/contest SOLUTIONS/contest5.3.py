string = input()
flag = False
is_printed = False
for i in string:
    if i.isdigit():
        flag = True
        is_printed = True
        print(i, end='')
    elif flag:
        flag = False
        print(" ", end='')
if not is_printed:
    print(-1)