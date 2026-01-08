N = int(input())
nums = list(map(int, input().split()))
li = list(map(int, input().split()))
operator = [] # +-x/

for i in range(4):
    for _ in range(li[i]):
        operator.append(i)

minimum = float('inf')
maximum = -float('inf')
visited = [False] * (N - 1)

def cal(n, result):
    if n == N:
        global minimum, maximum
        minimum = min(minimum, result)
        maximum = max(maximum, result)
    prev_op = -1
    for i in range(N-1):
        if visited[i]:
            continue
        if operator[i] == prev_op:
            continue
        prev_op = operator[i]
        visited[i] = True
        if operator[i] == 0:
            cal(n+1, result + nums[n])
        elif operator[i] == 1:
            cal(n+1, result - nums[n])
        elif operator[i] == 2:
            cal(n+1, result * nums[n])
        else:
            if result < 0:
                result = result * -1
                cal(n+1, (result // nums[n])*-1)
                result = result * -1
            else:
                cal(n+1, result // nums[n])
        visited[i] = False
cal(1, nums[0])
print(maximum)
print(minimum)