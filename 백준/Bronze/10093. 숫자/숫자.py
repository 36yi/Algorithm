a, b = map(int,input().split())
if a > b :
    a,b = b,a

if b - a <= 1:
    print(0)

else:
    print(b-a-1)
    for num in range(a+1,b):
        print(num, end = " ")