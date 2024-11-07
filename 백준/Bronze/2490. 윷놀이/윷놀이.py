dic = {3:'A',2:'B',1:'C',0:'D',4:'E'}
for _ in range(3):
    l = list(map(int,input().split()))
    print(dic[sum(l)])