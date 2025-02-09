#11652
import sys
input = sys.stdin.readline
t = int(input())
dic = {}
for _ in range(t):
    n = int(input())
    if(n in dic.keys()):
        dic[n] += 1
    
    else:
        dic[n] = 1

dic = sorted(dic.items(), key = lambda x : (x[0]))
dic = sorted(dic, key = lambda x : -x[1])


print(dic[0][0])