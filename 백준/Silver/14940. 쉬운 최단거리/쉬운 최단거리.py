from collections import deque

n, m = map(int, input().split())
board = []
visited = [[0] * m for _ in range(n)]
start_x = 0
start_y = 0
find = 0
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start_y, start_x = i, j
            find = 1
            break
    if find:
        break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([(start_x, start_y)])
visited[start_y][start_x] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
            
for i in range(n):
    print(*visited[i])
