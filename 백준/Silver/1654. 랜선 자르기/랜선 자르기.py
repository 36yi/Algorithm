N, K = map(int, input().split())
li = []

for _ in range(N):
    li.append(int(input()))

m = max(li)
r = m
l = 1
result = 0
while l <= r:
    length = (l+r)//2
    cnt = 0
    for i in range(N):
        cnt += li[i]//length

    if cnt < K:
        r = length - 1

    else:
        result = length
        l = length + 1
print(result)