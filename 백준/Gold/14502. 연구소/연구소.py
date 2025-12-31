import sys
input = sys.stdin.readline

from collections import deque
import copy

N, M = map(int, input().split())
origin = []
for _ in range(N):
    origin.append(list(map(int, input().split())))

dirs = ((0,1), (1,0), (0,-1), (-1,0))

def bfs(i,j,visited,board):
    queue = deque([(i,j)])
    visited[i][j] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if board[nr][nc] != 0:
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                board[nr][nc] = 2
                queue.append((nr,nc))


def count(board):
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if board[i][j] == 2:
                bfs(i,j,visited,board)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    return cnt

m = 0
li = []
for i in range(N):
    for j in range(M):
        if origin[i][j] == 0:
            li.append((i, j))
board = copy.deepcopy(origin)
for i in range(len(li)):
    board[li[i][0]][li[i][1]] = 1

    for j in range(i+1,len(li)):
        board[li[j][0]][li[j][1]] = 1

        for k in range(j+1,len(li)):
            board[li[k][0]][li[k][1]] = 1
            c = count(copy.deepcopy(board))
            m = max(c,m)
            board[li[k][0]][li[k][1]] = 0

        board[li[j][0]][li[j][1]] = 0

    board[li[i][0]][li[i][1]] = 0

print(m)