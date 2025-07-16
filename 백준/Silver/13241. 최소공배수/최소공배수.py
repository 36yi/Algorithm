def gcd(x,y):
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

a, b = map(int, input().split())
x = gcd(a, b)

print(x * (a//x) * (b//x))