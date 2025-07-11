from collections import defaultdict
n= int(input())
m = int(input())
board = defaultdict(list)
visited = []
for i in range(m):
    x , y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

def dfs(ind):
    visited.append(ind)
    for i in board[ind]:
        if i not in visited:
            dfs(i)

dfs(1)
print(len(visited)-1)