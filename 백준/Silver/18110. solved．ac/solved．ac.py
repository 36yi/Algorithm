import sys
input = sys.stdin.readline
def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
cut = my_round(n * 0.15)
li = []

for _ in range(n):
    li.append(int(input()))
li.sort()
li = li[cut:n-cut]

if len(li) == 0:
    print(0)
else:
    print(my_round(sum(li)/len(li)))