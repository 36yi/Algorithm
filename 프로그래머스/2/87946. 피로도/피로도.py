maximum = 0
def dfs(cnt, n, remain, dungeons,visited):
    flag = True
    global maximum
    if cnt == n:
        maximum = n
        
    for i in range(n):
        if visited[i]:
            continue
        if dungeons[i][0] <= remain:
            visited[i] = True
            flag = False
            dfs(cnt+1,n,remain - dungeons[i][1], dungeons,visited)
            visited[i] = False
            
    if flag:
        maximum = max(maximum,cnt)
        
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = -1
    dfs(0,n,k, dungeons,visited)
    print(maximum)
    return maximum