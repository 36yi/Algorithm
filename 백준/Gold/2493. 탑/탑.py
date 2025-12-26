n = int(input())
top = list(map(int, input().split()))
stack = []
ans = [0]*n
for i in range(n):
    while stack and top[stack[-1]] < top[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1] + 1
    stack.append(i)
print(*ans)