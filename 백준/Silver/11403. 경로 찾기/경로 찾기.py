import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * N
    while q:
        z = q.popleft()
        for i in range(N):
            if graph[z][i] == 1 and visited[i] == 0:
                visited[i] = 1
                graph[x][i] = 1
                q.append(i)


for i in range(N):
    bfs(i)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()