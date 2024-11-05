#Kiwi
# capacities = list(map(int,input().split()))
# bottles = list(map(int,input().split()))
# fromId = list(map(int,input().split()))
# toId = list(map(int,input().split()))
#
# returns = []
#
# for i in range(len(fromId)):
#     if bottles[fromId[i]] == 0:
#         continue
#     else:
#         if bottles[toId[i]] == capacities[toId[i]]:
#             continue
#
#         else:
#             s = bottles[fromId[i]] + bottles[toId[i]]
#             bottles[toId[i]] = min(capacities[toId[i]], bottles[toId[i]] + bottles[fromId[i]])
#             bottles[fromId[i]] = s - bottles[toId[i]]
#
# print(*bottles)

#Party

