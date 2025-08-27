import sys
input = sys.stdin.readline

n = int(input())
s = int(input())
p = input()
flag = False
prev_char = p[0]
start_ind = 0
cnt = 0
ans = 0

for i in range(s):
    if not flag:
        if p[i] == 'I':
            flag = True
    else:
        if prev_char == p[i]:
            if p[i] == 'I':
                pass
            else:
                flag = False
            cnt = 0
        else:
            if p[i] == 'I':
                if cnt == n:
                    ans += 1
                else:
                    cnt += 1
                    if cnt == n:
                        ans += 1
            else:
                pass
    prev_char = p[i]


print(ans)