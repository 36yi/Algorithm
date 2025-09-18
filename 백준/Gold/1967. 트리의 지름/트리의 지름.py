import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

max_length = 0

def dfs(node_index):
    for v, w in graph[node_index]:
        if visited[v] == -1:
            visited[v] = visited[node_index] + w
            dfs(v)

visited = [-1] * (n+1)
visited[1] = 0
dfs(1)

max_index = visited.index(max(visited))
visited = [-1] * (n+1)
visited[max_index] = 0
dfs(max_index)

print(max(visited))