from collections import deque
import sys
input = sys.stdin.readline

dirs = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(i,j,visited,land):
    N = len(land)
    M = len(land[0])
    w = 0
    left = j
    right = j
    queue = deque([(i,j)])
    visited[i][j] = True
    w += 1
    while queue:
        r,c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
                
            if visited[nr][nc]:
                continue
                
            if land[nr][nc] == 1:
                w += 1
                visited[nr][nc] = True
                queue.append((nr,nc))
                if nc < left :
                    left = nc
                elif nc > right:
                    right = nc
                    
    return left,right,w
        
def solution(land):
    N = len(land)
    M = len(land[0])
    li = [0] * M
    answer = 0
    visited = [[False] * M for _ in range(N)]
    for j in range(M):
        for i in range(N):
            if visited[i][j]:
                continue
            if land[i][j] == 1:
                l,r,w = bfs(i,j,visited,land)
                for k in range(l,r+1):
                    li[k] += w
                    
    answer = max(li)
    return answer