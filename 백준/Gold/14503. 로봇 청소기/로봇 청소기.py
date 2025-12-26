n, m = map(int, input().split())
r,c, direction = map(int, input().split()) # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
board = []
cnt = 0
for _ in range(n):
    board.append(list(map(int, input().split())))
    
move_reverse = ((1,0),(0,-1),(-1,0),(0,1))
move = ((-1,0),(0,1),(1,0),(0,-1))

def check(row,column):
    for dr, dc in move:
        next_row = row + dr
        next_column = column + dc
        if next_row < 0 or next_row >= n or next_column < 0 or next_column >= m:
            continue
        if board[next_row][next_column] == 0:
            return True

    return False

while True:
    if board[r][c] == 0:
        board[r][c] = -1
        cnt +=1

    if check(r,c):
        while True:
            direction = (direction - 1) % 4
            next_row = r + move[direction][0]
            next_column = c + move[direction][1]
            if next_row < 0 or next_row >= n or next_column < 0 or next_column >= m:
                continue
            if board[next_row][next_column] == 0:
                r = next_row
                c = next_column
                break
    else:
        next_row = r + move_reverse[direction][0]
        next_column = c + move_reverse[direction][1]
        if next_row < 0 or next_row >= n or next_column < 0 or next_column >= m:
            break
        if board[next_row][next_column] == 1:
            break
        r = next_row
        c = next_column

print(cnt)