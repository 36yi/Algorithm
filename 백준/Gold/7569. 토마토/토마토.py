import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
board = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        board[i].append(list(map(int, input().split())))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append((i,j,k))
while q:
    x,y,z = q.popleft()
    for i in range(6):
        nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
            if board[nx][ny][nz] == 0:
                board[nx][ny][nz] = board[x][y][z] + 1
                q.append((nx,ny,nz))
m = -2
flag = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                flag = True
                break
            elif board[i][j][k] == -1:
                pass
            else:
                m = max(m, board[i][j][k])
        if flag:
            break
    if flag:
        break

if flag:
    print(-1)

else:
    print(m-1)