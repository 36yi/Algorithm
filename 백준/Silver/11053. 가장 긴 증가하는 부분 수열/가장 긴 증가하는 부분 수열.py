n = int(input())
num = list(map(int,input().split()))
dp = [1]*n

for i in range(n):
    li = []
    for j in range(i):
        if(num[j] < num[i]):
            li.append(dp[j])
    if(len(li) != 0):
        dp[i] += max(li)


print(max(dp))