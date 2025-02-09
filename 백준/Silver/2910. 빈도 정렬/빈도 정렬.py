from collections import defaultdict

n, c = map(int,input().split())
nums = list(map(int,input().split()))
table_count = defaultdict(int)
table_find = {}

for i in range(n):
    table_count[nums[i]] += 1

    if nums[i] not in table_find:
        table_find[nums[i]] = i

nums.sort(key = lambda x : table_find[x])
nums.sort(key=lambda x: table_count[x], reverse=True)
print(*nums)