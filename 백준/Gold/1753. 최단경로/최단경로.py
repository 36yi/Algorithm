import sys
input = sys.stdin.readline

import heapq
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v, w))

INF = 1e8
distance = [INF] * (V + 1)

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        d, v = heapq.heappop(heap)
        for next_v, w in graph[v]:
            if distance[next_v] > w + distance[v]:
                distance[next_v] = w+ distance[v]
                heapq.heappush(heap, (distance[next_v], next_v))

dijkstra(K)
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])