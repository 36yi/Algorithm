import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
INF = float('inf')

graph = [[] for _ in range(V + 1)]

for _ in range(V):
    li = list(map(int, input().split()))
    u = li[0]
    i = 1
    while li[i] != -1:     
        v = li[i]
        w = li[i+1]
        graph[u].append((v, w))
        i += 2

def bfs(start):
    distance = [-1 for _ in range(V + 1)]
    distance[start] = 0
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node, weight in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = weight + distance[node]
                queue.append(next_node)

    far = 1
    for i in range(2, V + 1):
        if distance[i] > distance[far]:
            far = i

    return far, distance[far]

index, distance = bfs(1)
index, answer = bfs(index)
print(answer)



