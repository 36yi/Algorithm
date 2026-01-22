import sys
input = sys.stdin.readline

import heapq
N, K = map(int, input().split())
stuff = [tuple(map(int, input().split())) for _ in range(N)]
stuff.sort()
bags = [int(input()) for _ in range(K)]
bags.sort()

s = 0
heap = []
idx = 0
for cap in bags:
    while idx < N and stuff[idx][0] <= cap:
        heapq.heappush(heap, -stuff[idx][1])
        idx += 1
    if heap:
        s += -heapq.heappop(heap)
print(s)