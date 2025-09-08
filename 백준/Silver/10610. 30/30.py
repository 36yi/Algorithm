N = list(map(int, list(input())))

if 0 not in N or sum(N) % 3 != 0:
    print(-1)
    exit(0)

N.sort(reverse = True)
print(''.join(map(str, N)))