import sys
input = sys.stdin.readline

import heapq

N = int(input())
heap = []
for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if len(heap) > 0:
            x,y = heapq.heappop(heap)
            if y == -1:
                print( int(x+0.1)*(-1))
            else:
                print(x)
        else:
            print(0)

    elif cmd < 0:
        heapq.heappush(heap,((cmd+0.1)*(-1),-1))
    else:
        heapq.heappush(heap,(cmd,1))

