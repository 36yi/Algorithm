l = []
for _ in range(7):
    x = int(input())
    if (x % 2 == 1):
        l.append(x)
if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))