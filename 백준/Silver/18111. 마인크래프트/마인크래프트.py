import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
board = []
ma_x=0
mi_n = float('inf')
s = 0
for i in range(n):
    l = list(map(int, input().split()))
    ma_x = max(ma_x, max(l))
    mi_n = min(mi_n, min(l))
    s += sum(l)
    board.append(l)

min_time = float('inf')
height = 0
for i in range(mi_n, ma_x+1):
    t = 0
    remain = b
    if (n*m*i > b + s):
        continue

    else:
        for j in range(n):
            for k in range(m):
                if board[j][k] <= i:
                    t += i - board[j][k]
                else:
                    t += (board[j][k] - i) * 2
    if t < min_time:
        min_time = t
        height = i

    elif t == min_time:
        height = max(i,height)

print(min_time, height)