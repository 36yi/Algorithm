from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]





M, N = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j))

while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                q.append((ny,nx))

m = 0
flag = True
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            flag = False
        m = max(m, board[i][j])

if flag:
    print(m-1)
else:
    print(-1)