n,m = map(int,input().split())

cnt = 0
cnt += n-1
cnt += n*(m-1)

print(cnt)