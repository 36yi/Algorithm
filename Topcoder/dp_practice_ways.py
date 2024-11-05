# # 흠 이것도 dfs인가 그냥 재귀가 dfs인것인가
# # 재귀는 프로그래밍 기법 dfs는 탐색 알고리즘 풀이법
# cnt = 0
# def dfs (i, j, arrive_i, arrive_j):
#     global cnt
#
#     if(i > arrive_i or j > arrive_j):
#         return 0
#     if(i== arrive_i and j == arrive_j):
#         return 1
#     cnt += 1
#     return dfs(i+1,j, arrive_i,arrive_j) + dfs(i,j+1,arrive_i,arrive_j)
#
# print(dfs(0,0,5,4))
# print(cnt) #335
# #메모제이션 재귀
# w = 6
# h = 5
# memo = [[0] * w for _ in range(h)]
# cnt = 0
# def func(i,j):
#     global cnt
#     if(i >= 5 or j >= 6):
#          return 0
#
#     if memo[i][j] != 0:
#         return memo[i][j]
#
#     if(i == 4 and j == 5):
#         return 1
#     cnt += 1
#     memo[i][j] = func(i+1,j) + func(i,j+1)
#     return memo[i][j]
#
# print(func(0,0))
#
# print(cnt) # 29

#동적계획법 얘도 cnt 29임 dp[0][0] 지정해줬으니까
dp = [ [0] * 6 for _ in range(5)]

dp[0][0] = 1
for i in range(5):
    for j in range(6):
        if(i != 0):
            dp[i][j] += dp[i-1][j]
        if(j != 0):
            dp[i][j] += dp[i][j-1]
print(dp[i][j])