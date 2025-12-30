# bfs를 계속 때리고 한번 bfs하는게 1임
# bfs로 연결된부분 찾아서 평균내야함
from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
dirs = ((0,1), (1,0), (0,-1), (-1,0))

def bfs(i,j,visited):
    f = False # 바뀐게 있나 확인
    queue = deque([])
    queue.append((i, j))
    li = [(i, j)]
    s = board[i][j]
    visited[i][j] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if not visited[nr][nc]:
                if L <= abs(board[nr][nc] - board[r][c]) <= R:
                    f = True
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    li.append((nr, nc))
                    s += board[nr][nc]

    result = s // len(li)
    for k, l in li:
        board[k][l] = result
    return f # 바뀐게 있따면 true

day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    changed = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag = bfs(i, j, visited)
                if not changed:
                    changed = flag

    if not changed:
        break
    else:
        day += 1

print(day)