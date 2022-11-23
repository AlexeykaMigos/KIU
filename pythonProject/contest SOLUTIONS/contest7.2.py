lst = list(map(int, input().split()))
s = set()
for i in lst:
    if i not in s:
        s.add(i)
        print('NO')
    else:
        print('YES')