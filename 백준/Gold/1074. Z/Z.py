N,r,c = map(int, input().split())

def divide(p,i,j,order):
    if p == 0:
        return order

    ni = i
    nj = j
    if 2**(p-1) <= i:
        ni = i - 2**(p-1)
        order += (2**p ) * (2**(p-1))

    if 2**(p-1) <= j:
        nj = j - 2**(p-1)
        order += (2**(p-1) ) * (2**(p-1))

    return divide(p-1,ni,nj,order)

print(divide(N,r,c,0))