from collections import deque

c, r = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

queue = deque([])
for i in range(r):
    for j in range(c):
        if board[i][j] == 1:
            start_row, start_col = i, j
            queue.append((i, j, 0))

dr = (0,1,0,-1)
dc = (1,0,-1,0)


while queue:
    row, col, day = queue.popleft()
    for i in range(4):
        next_row, next_col = row + dr[i], col + dc[i]
        if 0 <= next_row < r and 0 <= next_col < c:
            if board[next_row][next_col] == 0:
                board[next_row][next_col] = day+1
                queue.append((next_row, next_col,day+1))

m = 0
f = True
for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            f = False
            print(-1)
            break
        else:
            if m < board[i][j]:
                m = board[i][j]
    if f == False:
        break
if f:
    if m == 1:
        print(0)
    else:
        print(m)