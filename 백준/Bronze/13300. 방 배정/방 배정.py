n, k = map(int,input().split())
li = [[0,0] for _ in range(6)]

for _ in range(n):
    s,y = map(int,input().split())
    li[y-1][s] += 1

cnt = 0
for i in range(6):
    for j in range(2):
        cnt += li[i][j]//k
        if li[i][j] % k != 0:
            cnt += 1

print(cnt)