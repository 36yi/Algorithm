from collections import deque
n, m, v = map(int,input().split())

graph = {}
for i in range(n):
  graph[i+1]=[]

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


for i in range(n):
  graph[i+1].sort()

def dfs_recursive(graph,start,visited=[]):
  visited.append(start)
  for node in (graph[start]):
    if node not in visited:
      dfs_recursive(graph,node,visited)
  return visited

visited=dfs_recursive(graph,v)
print(*visited)

def bfs(graph,start,visited=[]):
  queue = deque([start])
  visited.append(start)

  while queue:
    start = queue.popleft()
    for i in graph[start]:
      if i not in visited:
        queue.append(i)
        visited.append(i)
  return visited

visited=bfs(graph,v)
print(*visited)
  
  