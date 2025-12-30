import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
board = []
visited = [[[float('inf')] * C for _ in range(R)] for __ in range(2)]
for _ in range(R):
    board.append(list(input()))

dirs = ((1,0), (-1,0), (0,1), (0,-1))
queue = deque([])
visited[0][0][0] = 1
queue.append((0, 0, 0)) # 세번째 인자는 벽을 부쉈는가 확인

while queue:
    r, c, f = queue.popleft()
    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if f:
                if board[nr][nc] == '0':
                    if visited[f][nr][nc] > visited[f][r][c] + 1:
                        visited[f][nr][nc] = visited[f][r][c] + 1
                        queue.append((nr, nc, 1))
            else:
                if board[nr][nc] == '1':
                    if visited[1][nr][nc] > visited[f][r][c] + 1:
                        visited[1][nr][nc] = visited[f][r][c] + 1
                        queue.append((nr, nc, 1))
                else:
                    if visited[f][nr][nc] > visited[f][r][c] + 1:
                        visited[f][nr][nc] = visited[f][r][c] + 1
                        queue.append((nr, nc, 0))

if visited[0][R-1][C-1] == float('inf') and visited[1][R-1][C-1] == float('inf'):
    print(-1)
else:
    print(min(visited[0][R-1][C-1], visited[1][R-1][C-1]))