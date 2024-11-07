n = int(input())

li = list(map(int, input().split()))

y = 0
m = 0
for l in li:

    y += ((l // 30) + 1) * 10

    m += ((l // 60) + 1) * 15

if y < m:
    print(f"Y {y}")
elif y == m:
    print(f"Y M {y}")
else:
    print(f"M {m}")


