N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'Y':
            graph[i][j] = 1
        else:
            graph[i][j] = float('inf')

for k in range(N):
    for i in range(N):
        if i == k:
            continue
        for j in range(N):
            if j == k or i == j:
                continue

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


m= 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if graph[i][j] <= 2:
            cnt += 1
    m = max(m, cnt)
print(m)