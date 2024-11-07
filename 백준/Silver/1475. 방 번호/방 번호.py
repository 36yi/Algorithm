li = [0,0,0,0,0,0,0,0,0,0]
n = input()
for c in n:
    c = int(c)
    li[c] += 1

s = li[6] + li[9]
li[6] = s//2
li[9] = s - li[6]

print(max(li))