from collections import deque
start, target = map(int, input().split())
MAX = 200001
visited = [float("inf")] * MAX
q = deque()
q.append((start,0))
visited[start] = 0
while q:
    crnt, time = q.popleft()

    next = crnt + 1
    if 0 <= next < MAX and time + 1 < visited[next]:
        visited[next] = time + 1
        q.append((next, time + 1))

    next = crnt - 1
    if 0 <= next < MAX and time + 1 < visited[next]:
        visited[next] = time + 1
        q.append((next, time + 1))

    next = crnt * 2
    if 0 <= next < MAX and time < visited[next]:
        visited[next] = time
        q.append((next, time))

print(visited[target])