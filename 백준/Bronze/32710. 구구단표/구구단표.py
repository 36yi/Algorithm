s = set()
s.add(1)
for i in range(2,10):
    for j in range(1,10):
        s.add(i*j)
        
        
n = int(input())
if n in s:
    print(1)
else:
    print(0)