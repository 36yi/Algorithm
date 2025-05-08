import sys
input = sys.stdin.readline
li = set()
n = int(input())
for i in range(n):
    a,b = input().split()
    if b == "enter":
        li.add(a)
    else:
        li.remove(a)
       
li = list(li)
li.sort(reverse = True)
print(*li)