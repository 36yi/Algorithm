# 전체 탐색으로 풀기
# m = 0
# weight_list = [3,4,1,2,3]
# worth_list = [2,3,2,3,6]
# maxweight = 10
# def dfs(index ,weight,worth):
#     global m, maxweight
#     if(weight > maxweight):
#         return
#
#     if (m < worth): # index 가 5일때도 바꿔줘야함 왜냐면 이 worth는 index가 4일떄의 것을 반영한 것
#         m = worth
#     if(index == len(weight_list)):
#         return
#
#     dfs(index + 1, weight + weight_list[index], worth + worth_list[index])
#     dfs(index + 1, weight,worth)
#
# dfs(0,0,0)
# print(m)

#근데 이건 메모가 안되지 않나
#dfs 함수 방식을 변경하고 메모지에이션 해주기 메모 배열 크기나 모양을 잘 생각해야함
# ws = [3,4,1,2,3]
# ps = [2,3,2,3,6]
# max_weight = 10
# dp = [ [0] * (max_weight + 1) for _ in range(len(ws) + 1)]
#
# def dfs(n, w):
#     if w > max_weight:
#         return -10000  # 무게 초과 시 큰 음수 반환 return -1 하면 오류걸림 왜냐면 -1+ps[n]값이 더 큰 경우도 있기 때문 확실히 큰 음수로
#     if n >= len(ws):
#         return 0
#     if dp[n][w] != 0:
#         return dp[n][w]
#     dp[n][w] = max(dfs(n + 1, w), dfs(n + 1, w + ws[n]) + ps[n])
#     return dp[n][w]
#
# print(dfs(0,0))  # 출력: 14

#동적
# dp = [[0] * 11 for _ in range(6) ]
# ws = [3,4,1,2,3]
# ps = [2,3,2,3,6]
# m = 0
# for i in range(5):
#     for j in range(11):
#         if(j + ws[i] > 10):
#             continue
#         else:
#             dp[i+1][j + ws[i]] = max(dp[i+1][j+ws[i]], dp[i][j] + ps[i])
#             m = max(m, dp[i+1][j + ws[i]])
# print(m)
# for i in range(5):
#     print(*dp[i])
# 관점을 다르게
ws = [3,4,1,2,3]
ps = [2,3,1,3,6]
max_weight = 10
dp = [[10000] * 16 for _ in range(6)]

m = 0
dp[0][0] = 0
for i in range(5):
    for j in range(16):
        if(j + ps[i] < 16):
            if dp[i][j] != 10000:
                dp[i+1][j+ps[i]] = min(dp[i+1][j+ps[i]], dp[i][j] + ws[i])
                dp[i+1][j] = min(dp[i][j],dp[i+1][j])

for i in range(6):
    for j in range(16):
        if(dp[i][j] < max_weight):
            m = max(m,j)
        if(dp[i][j] == 10000):
            dp[i][j] = -1
print(m)
for i in range(6):
    print(*dp[i])

