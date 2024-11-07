n = int(input())
for _ in range(n):
    x, y = input().split()
    li = [0]*26
    flag = 1

    for c in x:
        li[ord(c)-ord('a')] += 1
    for c in y:
        if li[ord(c)-ord('a')] == 0:
            flag = 0
            break
        li[ord(c)-ord('a')] -= 1

    if flag :
        if li.count(0) == 26:
            print("Possible")
        else:
            print("Impossible")
    else:
        print("Impossible")
