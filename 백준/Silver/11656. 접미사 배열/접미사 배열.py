# 11656
a = input()
li = [a]
for i in range(len(a) - 1):
    li.append(a[i+1:])

li.sort()
for i in li:
    print(i)