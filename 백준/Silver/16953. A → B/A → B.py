from collections import deque
a, b = map(int, input().split())
q = deque()
q.append((a,0))
f = True
while q:
    n,cnt = q.popleft()
    if n*10 + 1 == b or n*2 == b:
        print(cnt+2)
        f = False
        break

    if n*2 < b:
        q.append((n*2,cnt+1))

    if n*10 + 1 < b:
        q.append((n*10+1,cnt+1))

if f:
    print(-1)