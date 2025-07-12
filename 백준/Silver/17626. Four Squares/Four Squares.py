from collections import deque
n = int(input())
visited = [False] * (n+1)
q = deque()
q.append((n,0))
visited[n] = True
while q:
    num,cnt = q.popleft()
    x = num ** (1/2)
    x = int(x)
    for i in range(int(num ** 0.5), 0, -1): 
        next_num = num - i * i
        if next_num == 0:
            print(cnt + 1)
            exit()
        if not visited[next_num]:
            visited[next_num] = True
            q.append((next_num, cnt + 1))


