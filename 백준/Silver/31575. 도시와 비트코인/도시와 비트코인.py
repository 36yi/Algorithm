from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
target_x = M - 1
target_y = N - 1
board = []
visited = [[False] * M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

q = deque()
q.append((0,0))
visited[0][0] = True

d = ((0,1),(1,0))
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] == 1:

            q.append((nx, ny))
            visited[ny][nx] = True


if visited[target_y][target_x]:
    print("Yes")
else:
    print("No")