str = input()
ans = ''
operator = []

for s in str:
    if s.isalpha():
        ans += s

    else:
        if s == '(':
            operator.append(s)

        elif s == '*' or s =='/':
            while operator:
                if operator[-1] == '*' or operator[-1] == '/':
                    ans += operator.pop()
                else:
                    break
            operator.append(s)
        elif s == '+' or s == '-':
            while operator:
                if operator[-1] == '(':
                    break
                else:
                    ans += operator.pop()
            operator.append(s)
        else:
            while operator:
                if operator[-1] == '(':
                    operator.pop()
                    break
                else:
                    ans += operator.pop()
while operator:
    ans+=(operator.pop())

print(ans)
