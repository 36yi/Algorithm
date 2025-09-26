T = int(input())
INF = float('inf')

for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []

    for __ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a,b,c))
        edges.append((b,a,c))

    for __ in range(W):
        a, b, c = map(int, input().split())
        c = -c
        edges.append((a,b,c))

    distance = [0] * (N+1)

    distance[1] = 0
    flag = True
    for i in range(N):
        for a,b,c in edges:
            if distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == N-1:
                    flag = False
                    break

    if flag:
        print("NO")
    else:
        print("YES")