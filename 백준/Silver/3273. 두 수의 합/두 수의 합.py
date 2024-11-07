cnt = 0
n = int(input())
nums = list(map(int,input().split()))
x = int(input())

li = [0] * 1000001
for num in nums:
    li[num] = 1

for num in nums:
    if 0<=x-num<=1000000 and li[x-num]:
        cnt += 1

print(cnt//2)