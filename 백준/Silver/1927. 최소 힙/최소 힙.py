import heapq
import sys
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    x = int(input())
    if x == 0:
        if len(li) == 0:
            print(0)
        else:
            print(heapq.heappop(li))
    else:
        heapq.heappush(li, x)
    
