import sys
input = sys.stdin.readline

from collections import deque
wheel = [deque(list(input().rstrip())) for _ in range(4)]
K = int(input())

def rotate(f, num, direction):
    right = wheel[num][2]
    left = wheel[num][-2]
    wheel[num].rotate(direction)

    if num == 0 or num == 1 or num == 2:
        if f == num + 1:
            pass
        elif right != wheel[num+1][-2]:
            rotate(num,num+1, direction*-1)

    if num == 3 or num == 1 or num == 2:
        if f == num - 1:
            pass
        elif left != wheel[num-1][2]:
            rotate(num, num-1, direction*-1)

for _ in range(K):
    num, dir = map(int, input().split())
    rotate(num-1, num-1 , dir)

s = 0
for i in range(4):
    s += int(wheel[i][0]) * (2 ** i)

print(s)