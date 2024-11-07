l = [ i for i in range(1,21)]
for _ in range(10):
    a, b = map(int,input().split())
    small = l[a-1:b]
    small.reverse()
    l[a-1:b] = small
print(*l)



