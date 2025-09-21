import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    heapq.heappush(heap, (0,start))

    while heap:
        crnt_weight, crnt_node = heapq.heappop(heap)

        if crnt_weight > distance[crnt_node]:
            continue

        for neighbor, weight in graph[crnt_node]:
            if weight + crnt_weight < distance[neighbor]:
                distance[neighbor] = weight + crnt_weight
                heapq.heappush(heap, (distance[neighbor], neighbor))

    return distance

for i in range(1,n+1):
    heap = []
    ans = dijkstra(i)
    for j in range(1,n+1):
        if ans[j] == float('inf'):
            print(0,end=' ')
        else:
            print(ans[j],end=' ')

    print()