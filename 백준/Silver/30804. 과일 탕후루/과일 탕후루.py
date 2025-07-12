from collections import defaultdict
n = int(input())
li = list(map(int, input().split()))
l = 0
cnt = defaultdict(int)
max_len = 0
for i in range(n):
    cnt[li[i]] += 1
    while len(cnt.keys()) > 2:
        cnt[li[l]] -= 1
        if cnt[li[l]] == 0:
            del cnt[li[l]]
        l += 1
    max_len = max(max_len, i-l+1)
print(max_len)