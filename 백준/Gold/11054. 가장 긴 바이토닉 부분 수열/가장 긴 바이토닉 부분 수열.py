n = int(input())
nums = list(map(int,input().split()))
nums2 = list(reversed(nums))

dp = [1]*n
dp2 = [1]*n
for i in range(n):
    li = []
    li2 = []
    for j in range(i):
        if(nums[j] < nums[i]):
            li.append(dp[j])

        if(nums2[j] < nums2[i]):
            li2.append(dp2[j])

    if(len(li) != 0):
        dp[i] += max(li)
    
    if(len(li2) != 0):
        dp2[i] += max(li2)

ans = []
for i in range(n):
    ans.append(dp[i] + dp2[n-1-i])


print(max(ans) - 1)