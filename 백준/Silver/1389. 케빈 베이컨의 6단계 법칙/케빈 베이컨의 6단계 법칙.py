import sys
input = sys.stdin.readline

from collections import defaultdict,deque
graph = defaultdict(set)
N, M = map(int, input().split())

def bfs(x, y):
    q = deque()
    q.append((x,1))
    visited = [0] * (N+1)

    while q:
        z, cnt = q.popleft()
        if y in graph[z]:
            break
        for i in graph[z]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, cnt + 1))
    return cnt

for i in range(M):
    a,b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

MIN = float("inf")
Min_ind = 0

for i in range(1,N+1):
    ans = 0
    for j in range(1,N+1):
        if i == j :
            continue
        ans += bfs(i, j)
    if ans < MIN:
        MIN = ans
        Min_ind = i

print(Min_ind)