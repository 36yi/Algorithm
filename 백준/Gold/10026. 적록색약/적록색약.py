import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i,j,color):
    for k, l in d:
        ni, nj = i + k, j + l

        if 0 <= ni < N and 0 <= nj < N:
            if check[ni][nj] == 0 and board[ni][nj] == color:
                check[ni][nj] = 1
                dfs(ni,nj,color)

N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

check = [[0]* N for _ in range(N)]
d = ((1,0),(-1,0),(0,-1),(0,1))
cnt = 0

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            check[i][j] = 1
            dfs(i,j,board[i][j])
            cnt += 1

print(cnt, end=" ")

for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'

cnt = 0
check = [[0]* N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            check[i][j] = 1
            dfs(i,j,board[i][j])
            cnt += 1
print(cnt)