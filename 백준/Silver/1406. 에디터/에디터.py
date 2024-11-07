import sys
input = lambda : sys.stdin.readline().rstrip()
# 1406
# 1406
s = list(input())
s2 = []
t = int(input())


for _ in range(t):
    cmd = input().split()
    c = len(s)
    c2 = len(s2)
    if(cmd[0] == 'L'):
        if(c == 0):
            pass
        else:
            s2.append(s.pop())
    elif(cmd[0] == 'D'):
        if(c2 == 0):
            pass
        else:
            s.append(s2.pop())

    elif(cmd[0] == 'B'):
        if(c == 0):
            pass
        else:
            s.pop()
            
    else:
        s.append(cmd[1])
s2.reverse()
ans = s + s2
print(''.join(ans))
