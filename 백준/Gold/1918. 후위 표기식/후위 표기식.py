import sys
pri = {'+': 0, '-':0, '*':1, '/': 1, '(':2, ')':2}
input = sys.stdin.readline
STR = list(input().rstrip())
operator = []
ans = []

for i in range(len(STR)):
    if STR[i] not in pri.keys():
        ans.append(STR[i])

    else:
        if len(operator) == 0:
            operator.append(STR[i])

        elif STR[i] == ')':
            while operator:
                x = operator.pop()
                if x == '(':
                    break

                ans.append(x)

        elif pri[operator[-1]] >= pri[STR[i]] and operator[-1] != '(':
            mark = pri[STR[i]]
            while operator:
                x = operator.pop()
                if pri[x] >= mark and x != '(':
                    ans.append(x)
                else:
                    operator.append(x)
                    break
            operator.append(STR[i])
        else:
            operator.append(STR[i])

while operator:
    x = operator.pop()
    ans.append(x)

print(''.join(ans))