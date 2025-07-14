n = int(input())
l = []
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    x = min(a, b, n - a + 1, n - b + 1)
    if x % 3 == 0:
        print(3)
    else:
        print(x % 3)