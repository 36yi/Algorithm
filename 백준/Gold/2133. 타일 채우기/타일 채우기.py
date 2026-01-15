#2133
n = int(input())
dp = [0]*(n+1)
if(n % 2 == 1):
    print(0)

else:
    if(n == 2):
        print(3)
    else:
        dp[2] = 3
        for i in range(4,n+1):
            if(i%2 == 1):
                pass
            else:
                dp[i] = dp[i-2] * 3 + sum(dp[:i-3])*2 + 2

        print(dp[n])