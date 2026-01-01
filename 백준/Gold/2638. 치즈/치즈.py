import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 가장자리에 치즈가 없다했으니까 바깥 공기 부분을 기록하는게 필요
# 그래서 치즈 없애고 라운드별로 또 공기 체크하고 반복..

dirs = ((0,1),(1,0),(0,-1),(-1,0))

def check_out(i,j,board):
    queue = deque()
    board[i][j] = -1
    queue.append((i,j))

    while queue:
        r,c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if board[nr][nc] == 0:
                board[nr][nc] = -1
                queue.append((nr,nc))

check_out(0,0,board)

day = 0

while True:
    flag = True
    for i in range(N):
        for j in range(M):
            cnt = 0
            if board[i][j] == 1:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < M):
                        continue
                    if board[ni][nj] == -1:
                        cnt += 1
                if cnt >= 2:
                    flag = False
                    board[i][j] = 0
    if flag:
        break

    day += 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < M):
                        continue
                    if board[ni][nj] == -1:
                        check_out(i,j,board)
                        break
print(day)