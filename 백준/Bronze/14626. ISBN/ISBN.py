s = input()
x = 0
sum = 0
for i in range(13):
    if s[i] == '*':
        x = i
    else:
        if i % 2 == 0:
            sum += int(s[i]) * 1
        else:
            sum += int(s[i]) * 3

if x % 2 == 0:
    ans = 10 - (sum % 10)

else:
    for i in range(10):
        if (3*i + sum)% 10 == 0:
            ans = i
            break

print(ans)
