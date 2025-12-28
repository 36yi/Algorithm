import sys
input = sys.stdin.readline

from collections import defaultdict
import heapq

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)

    for __ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a,s))

    distance = [float('inf')] * (n+1)
    distance[c] = 0
    li = []
    heapq.heappush(li, (0, c))


    while li:
        d, v = heapq.heappop(li)
        for next, weight in graph[v]:
            if distance[next] > d + weight:
                distance[next] = d + weight
                heapq.heappush(li, (d + weight, next))

    cnt = 0
    m = 0
    for i in range(1,len(distance)):
        if distance[i] != float('inf'):
            cnt += 1
            if m < distance[i]:
                m = distance[i]

    print(cnt, m)