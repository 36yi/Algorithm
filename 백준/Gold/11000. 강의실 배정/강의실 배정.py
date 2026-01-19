import heapq
import sys
input = sys.stdin.readline
n = int(input())

task = []
for _ in range(n):
    task.append(tuple(map(int, input().split())))
task.sort(key=lambda x: x[0])

room = []
room.append(task[0][1])
heapq.heapify(room)
for i in range(1,n):
    s, e = task[i]
    if room[0] > s:
        heapq.heappush(room,e)
    else:
        x = heapq.heappop(room)
        heapq.heappush(room,e)

print(len(room))