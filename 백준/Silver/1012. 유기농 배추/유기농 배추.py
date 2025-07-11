import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(ind_x, ind_y, visited, m, n,board):
    visited.add((ind_x, ind_y))
    for i in range(4):
        if 0 <= ind_x + dx[i] < m and 0 <= ind_y + dy[i] < n:
            if (ind_x+dx[i], ind_y+dy[i]) not in visited:
                if board[ind_y+dy[i]][ind_x+dx[i]] == 1:
                    dfs(ind_x+dx[i], ind_y+dy[i], visited, m, n,board)

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
        visited = set()

    cnt = 0
    for j in range(M):
        for k in range(N):
            if board[k][j] == 1:
                if (j,k) not in visited:
                    dfs(j, k, visited, M, N, board)
                    cnt += 1
    print(cnt)
