dict = {}
n, m = map(int, input().split())
for i in range(n):
    site , pwd = input().split()
    dict[site] = pwd

for i in range(m):
    print(dict[input()])