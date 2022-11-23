string = input()
avg = 0
for i in string.split():
    avg += len(i)
avg /= len(string.split())
print(str(int(avg)) + "." + str(int((avg - int(avg)) * 100)))