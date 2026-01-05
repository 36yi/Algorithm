import sys
input = sys.stdin.readline

N, M = map(int, input().split())
home = []
chicken = []
board = []
m = N*N*N

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

def distance(s):
    res = 0
    for r1,c1 in home:
        d = float('inf')
        for x in s:
            r2,c2 = chicken[x]
            d = min(d, abs(r1-r2) + abs(c1-c2))
        res += d
    return res

def func(start,cnt, s):
    if cnt == M:
        global m
        m = min(m,distance(s))
        return

    for i in range(start,len(chicken)):
        if i in s:
            continue
        s.add(i)
        func(i+1,cnt+1, s)
        s.discard(i)

func(0,0,set())
print(m)