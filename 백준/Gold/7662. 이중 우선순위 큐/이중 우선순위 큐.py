import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    alive = {}
    uid = 0
    def clean_min():
        while min_heap and not alive.get(min_heap[0][1], False):
            heapq.heappop(min_heap)
    def clean_max():
        while max_heap and not alive.get(max_heap[0][-1], False):
            heapq.heappop(max_heap)

    for __ in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(min_heap, (n, uid))
            heapq.heappush(max_heap, (n * (-1), uid))
            alive[uid] = True
            uid += 1

        else:
            if len(min_heap) == 0 or len(max_heap) == 0:
                continue
            if n == 1:  # 최대값 제거
                clean_max()
                if max_heap:
                    asdf, id = heapq.heappop(max_heap)
                    alive[id] = False
            else:  # 최소값 제거
                clean_min()
                if min_heap:
                    asdf, id = heapq.heappop(min_heap)
                    alive[id] = False

    clean_min()
    clean_max()
    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print((-1)*max_heap[0][0],min_heap[0][0])