import sys
input = sys.stdin.readline

from collections import defaultdict

def dfs(start,ind,visited,flag):
    if start == ind and flag == True:
        return

    for i in graph[ind]:
        if i not in visited:
            visited.append(i)
            dfs(start,i,visited,True)


n = int(input())
graph = defaultdict(set)
li = []

for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if li[i][j] != 0:
            graph[i].add(j)
for i in range(n):
    v = []
    dfs(i,i,v,False)
    graph[i] |= set(v)

for i in range(n):
    for j in range(n):
        if j in graph[i]:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()