import sys
input = sys.stdin.readline

N, M = map(int, input().split())
CCTV = []
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 or board[i][j] == 6:
            continue
        else:
            CCTV.append((i,j))

dirs = ((1,0),(0,1),(-1,0),(0,-1))
minimum = float('inf')

def fill(r,c, dir):
    while True:
        r,c = r + dirs[dir][0], c + dirs[dir][1]
        if not (0 <= r < N and 0 <= c < M):
            break
        if board[r][c] == 6:
            break
        if board[r][c] <= 0:
            board[r][c] -= 1

def erase(r,c,dir):
    while True:
        r, c = r + dirs[dir][0], c + dirs[dir][1]
        if not (0 <= r < N and 0 <= c < M):
            break
        if board[r][c] == 6:
            break
        if board[r][c] < 0:
            board[r][c] += 1

def dfs(index):
    if index == len(CCTV):
        global minimum
        x = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    x += 1
        minimum = min(minimum, x)
        return

    r = CCTV[index][0]
    c = CCTV[index][1]
    cctv_type = board[r][c]

    if cctv_type == 1:
        for i in range(4):
            fill(r,c,i)
            dfs(index + 1)
            erase(r,c,i)
    elif cctv_type == 2:
        for i in range(2):
            fill(r,c,i)
            fill(r,c,i+2)
            dfs(index + 1)
            erase(r,c,i+2)
            erase(r,c,i)
    elif cctv_type == 3:
        for i in range(4):
            fill(r,c,i%4)
            fill(r,c,(i+1)%4)
            dfs(index + 1)
            erase(r,c,i%4)
            erase(r,c,(i+1)%4)
    elif cctv_type == 4:
        for i in range(4):
            fill(r,c,i%4)
            fill(r,c,(i+1)%4)
            fill(r,c,(i+2)%4)
            dfs(index + 1)
            erase(r,c,i%4)
            erase(r,c,(i+1)%4)
            erase(r, c, (i+2) % 4)
    else:
        for i in range(4):
            fill(r,c,i)
        dfs(index + 1)
        for i in range(4):
            erase(r,c,i)

dfs(0)
print(minimum)