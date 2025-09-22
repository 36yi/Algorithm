import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split()) # X : target
graph = [[] for _ in range(N+1)]
MAX = float('inf')

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    heap = []
    distance = [MAX] * (N+1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distance[node]:
            continue

        for next_node, weight in graph[node]:
            if distance[next_node] > cost + weight:
                distance[next_node] = cost + weight
                heapq.heappush(heap, (distance[next_node], next_node))
    return distance

target_to_home = dijkstra(X)
max_time = 0
for i in range(1,N+1):
    if i == X:
        continue

    result = dijkstra(i)

    if result[X] + target_to_home[i] > max_time:
        max_time = result[X] + target_to_home[i]

print(max_time)