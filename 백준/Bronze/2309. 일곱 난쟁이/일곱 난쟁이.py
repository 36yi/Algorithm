l = []
for _ in range(9):
    l.append(int(input()))

flag = 0
s = sum(l)
for i in range(len(l) - 1):
    num = s - l[i]
    for j in range(i + 1, len(l)):
        x = num - l[j]
        if (x == 100):
            l.pop(j)
            flag = 1
            break

    if flag:
        l.pop(i)
        break

l.sort()
for i in range(len(l)):
    print(l[i])