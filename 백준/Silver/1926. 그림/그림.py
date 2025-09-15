import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

visited = [[False] * m for _ in range(n)]
d = ((0,1),(1,0),(-1,0),(0,-1))
max_area = 0
area = 0

def dfs(i, j):
    global area

    for d_col, d_row in d:
        next_row, next_col = i + d_row, j + d_col
        if 0 <= next_row < n and 0 <= next_col < m:
            if board[next_row][next_col] == 1 and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                area += 1
                dfs(next_row, next_col)

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            area = 1
            visited[i][j] = True
            dfs(i, j)
            max_area = max(max_area, area)

print(cnt)
print(max_area)