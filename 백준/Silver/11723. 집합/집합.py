import sys
input =sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    cmd = input()
    if cmd[:3] == "all":
        s = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}
    elif cmd[:5] == "empty":
        s = set()
    else:
        cmd , x = cmd.split(" ")
        if cmd == "add":
            s.add(int(x))
        elif cmd == "remove":
            if int(x) in s:
                s.remove(int(x))
            else:
                pass
        elif cmd == "check":
            if int(x) in s:
                print(1)
            else:
                print(0)
        elif cmd =="toggle":
            if int(x) in s:
                s.remove(int(x))
            else:
                s.add(int(x))