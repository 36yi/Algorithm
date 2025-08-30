from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
check = [0] * 101
q = deque()
q.append((1,0))

for _ in range(N+M):
    x, y = map(int, input().split())
    dict[x] = y

while q:
    ind, cnt = q.popleft()
    for i in range(1,7):
        n = ind+i
        if n in dict:
            n = dict[n]

        if n == 100:
            print(cnt+1)
            exit(0)

        if check[n] == 0 or check[n] > cnt + 1:
            check[n] = cnt + 1
            q.append((n,cnt+1))