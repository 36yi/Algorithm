import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict

def dfs(ind):
    for i in graph[ind]:
        if visited[i] == 0:
            visited[i] = ind
            dfs(i)
n = int(input())
visited = [0] * (n+1)
visited[1] = 1
graph = defaultdict(list)
for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
for i in range(2, n+1):
    print(visited[i])