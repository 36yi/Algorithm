import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dp = [0] * (K+1) #dp[i]: i용량일 때 가질 수 있는 최대 가치 (누적 물건을 고려하여)
for _ in range(N):
    W, V = map(int,input().split())
    for i in range(K,W-1,-1):
        dp[i] = max(dp[i], dp[i-W] + V)
print(dp[K])