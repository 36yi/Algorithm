import sys
input = sys.stdin.readline

N = int(input())
graph = [[float('inf')]  * 26 for _ in range(26)]
for _ in range(N):
    a, b, c = input().split()
    graph[ord(a) - ord('a')][ord(c) - ord('a')] = 1

for i in range(26):
    graph[i][i] = 0

for k in range(26):
    for i in range(26):
        if k == i:
            continue

        for j in range(26):
            if k == j or j == i:
                continue

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

M = int(input())
for _ in range(M):
    a, b, c = input().split()
    if graph[ord(a) - ord('a')][ord(c) - ord('a')] != float('inf'):
        print('T')
    else:
        print('F')