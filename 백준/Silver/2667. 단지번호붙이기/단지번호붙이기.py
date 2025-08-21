from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

check = [[0] * n for i in range(n)]
apartment = []

def bfs(i,j):
    queue = deque([(i,j)])
    check[i][j] = 1
    length = 1

    while queue:
        ci, cj = queue.popleft()
        for k in range(4):
            nx = ci + dx[k]
            ny = cj + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '1' and check[nx][ny] == 0:
                length += 1
                queue.append((nx, ny))
                check[nx][ny] = 1

    apartment.append(length)



for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and check[i][j] == 0:
            bfs(i, j)

print(len(apartment))
apartment.sort()
for i in apartment:
    print(i)