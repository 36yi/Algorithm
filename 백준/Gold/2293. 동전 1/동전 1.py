import sys
input = sys.stdin.readline

n, K = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins = [c for c in coins if c<=K]
n = len(coins)
dp = [0] * (K+1)
dp[0] = 1
for coin in coins:
    for j in range(coin, K+1):
        dp[j] += dp[j-coin]

print(dp[K])