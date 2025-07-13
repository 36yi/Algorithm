import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
board = []
visited = [[0]*M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def dfs(i,j):
    visited[i][j] = 1
    if board[i][j] == 'P':
        global cnt
        cnt += 1

    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0 <= ni < N and 0 <= nj < M:
            if visited[ni][nj] == 1 or board[ni][nj] == 'X':
                continue
            dfs(ni,nj)

for _ in range(N):
    board.append(list(input()))

for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            dfs(i,j)

if cnt == 0:
    print("TT")
else:
    print(cnt)