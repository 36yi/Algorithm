import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

visited = [[[float('inf')] * M for _ in range(N)] for _ in range(2)]
q = deque()
q.append((0, 0, False))
visited[0][0][0] = 1
d = ((0,1),(1,0),(0,-1),(-1,0))

while q:
    crnt_row, crnt_col, used = q.popleft()
    for dr, dc in d:
        next_row, next_col = crnt_row + dr, crnt_col + dc
        if 0 <= next_row < N and 0 <= next_col < M:
            if used == False:
                if board[next_row][next_col] == '0' and visited[0][next_row][next_col] == float('inf'):
                    visited[0][next_row][next_col] = visited[0][crnt_row][crnt_col] + 1
                    q.append((next_row, next_col,used))
                else:
                    if visited[1][next_row][next_col] == float('inf'):
                        visited[1][next_row][next_col] = visited[0][crnt_row][crnt_col] + 1
                        q.append((next_row, next_col,True))
            else:
                if board[next_row][next_col] == '0' and visited[1][next_row][next_col] == float('inf'):
                    visited[1][next_row][next_col] = visited[1][crnt_row][crnt_col] + 1
                    q.append((next_row, next_col,used))
                else:
                    pass
                
m = min(visited[0][N-1][M-1], visited[1][N-1][M-1])
if m == float('inf'):
    print(-1)
else:
    print(m)