import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append(tuple(map(int, input().split())))

dp = [[0] * 3 for _ in range(2)]
dp2 = [[0] * 3 for _ in range(2)]

for i in range(n):
    for j in range(3):
        if i == 0:
            dp[i][j] = board[i][j]
            dp2[i][j] = board[i][j]
        else:
            dp_row = i % 2
            if j == 0:
                dp[dp_row][j] = max(dp[1 - dp_row][j], dp[1 - dp_row][j+1]) + board[i][j]
                dp2[dp_row][j] = min(dp2[1 - dp_row][j], dp2[1 - dp_row][j+1]) + board[i][j]
            elif j == 2:
                dp[dp_row][j] = max(dp[1 - dp_row][j-1], dp[1 - dp_row][j]) + board[i][j]
                dp2[dp_row][j] = min(dp2[1 - dp_row][j-1], dp2[1 - dp_row][j]) + board[i][j]
            else:
                dp[dp_row][j] = max(dp[1 - dp_row][j-1], dp[1 - dp_row][j], dp[1 - dp_row][j+1]) + board[i][j]
                dp2[dp_row][j] = min(dp2[1 - dp_row][j-1], dp2[1 - dp_row][j], dp2[1 - dp_row][j+1]) + board[i][j]

print(max(dp[(n+1)%2]),min(dp2[(n+1)%2]))