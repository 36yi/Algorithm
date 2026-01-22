import sys
input = sys.stdin.readline

n = int(input())
max_day = 0
clas = []

for _ in range(n):
    a, b= map(int, input().split())
    clas.append((a,b))

clas.sort(reverse=True)
cal = [0] * (10001)
for i in range(n):
    a,b = clas[i]
    for j in range(b,0,-1):
        if cal[j] == 0:
            cal[j] = a
            break

print(sum(cal))