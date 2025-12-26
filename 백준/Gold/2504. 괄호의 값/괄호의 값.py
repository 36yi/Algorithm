s = input()
stack = []
ans = []
depth = 0
f = False
def func(mul, depth):
    global ans

    sum_num = 0
    keep = []
    for i in range(len(ans)):
        num, d = ans[i]
        if d == depth + 1:
            sum_num += num
        else:
            keep.append((num,d))
    keep.append((sum_num * mul, depth))
    if sum_num == 0:
        keep.append((mul, depth))

    ans = keep

for i in range(len(s)):
    if s[i] == '(':
        stack.append((s[i]))
        depth += 1
    if s[i] == '[':
        stack.append(s[i])
        depth += 1

    if s[i] == ')':
        if len(stack) == 0:
            f = True
            break

        if stack[-1][0] =='(':
            stack.pop()
            depth -= 1
            func(2,depth)

        elif stack[-1][0] =='[':
            f = True
            break

    if s[i] == ']':
        if len(stack) == 0:
            f = True
            break

        if stack[-1][0] == '[':
            stack.pop()
            depth -= 1
            func(3,depth)

        elif stack[-1][0] == '(':
            f = True
            break
if stack:
    f = True

if f:
    print(0)
else:
    answer = 0
    for i in range(len(ans)):
        if ans[i][1] == 0:
            answer += ans[i][0]
    print(answer)