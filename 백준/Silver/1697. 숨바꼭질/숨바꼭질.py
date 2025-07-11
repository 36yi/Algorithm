import sys
input = sys.stdin.readline

from collections import deque
N, K = map(int, input().split())
min_time = float('inf')
x = max(N,K)
visited = [float('inf')] * (x*2 + 1)
def bfs(ind):
    queue = deque([ind])
    visited[ind] = 0
    while queue:
        current = queue.popleft()
        if 0 <= current - 1 :
            if visited[current] + 1 < visited[current - 1]:
                visited[current-1] = visited[current] + 1
                queue.append(current - 1)
        if current < K:
            if visited[current] + 1 < visited[current + 1]:
                visited[current + 1] = visited[current] + 1
                queue.append(current + 1)
            if visited[current] + 1 < visited[current *2 ]:
                visited[current * 2] = visited[current] + 1
                queue.append(current * 2)


bfs(N)
print(visited[K])