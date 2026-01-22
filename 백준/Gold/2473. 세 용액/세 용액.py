n = int(input())
li = list(map(int, input().split()))
li.sort()
minimum = float('inf')
same_flag= False
for i in range(n-2):
    left = i + 1
    right = n - 1
    while left < right:
        s = li[i] + li[left] + li[right]
        if minimum > abs(s):
            minimum = abs(s)
            result = (li[i], li[left], li[right])
        if s < 0:
            left += 1
        elif s == 0:
            same_flag = True
            break
        else:
            right -= 1
    if same_flag:
        break
print(*result)