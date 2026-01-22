import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homes = [int(input()) for _ in range(N)]
homes.sort()
hi = max(homes)-min(homes)
lo = 1
while hi >= lo:
    d = (lo+hi)//2
    index = 1
    prev = 0
    cnt = 1
    while index < N and cnt < C:
        if homes[index] - homes[prev] < d:
            index += 1
        else:
            prev = index
            index += 1
            cnt += 1
    if cnt == C:
        lo = d + 1
    else:
        hi = d - 1

print(hi)