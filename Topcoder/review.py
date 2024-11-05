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
# first = list(input().split())
# second = list(input().split())
# table = {}
# for i in first:
#     if i not in table:
#         table[i] = 1
#     else:
#         table[i] += 1
#
# for i in second:
#     if i not in table:
#         table[i] = 1
#     else:
#         table[i] += 1
#
# res = list(table.items())
# res.sort(key=lambda x: x[1], reverse=True)
# print(res[0][1])

# #Cryptography
# numbers = list(map(int,input().split()))
# m = []
# multi = 1
# for num in numbers:
#     multi *= num
#
# for num in numbers:
#     m.append(multi//num*(num+1))
# print(max(m))

#InterestingDigits
# base = int(input())
#
# res = []
# for j in range(2,base):
#     i = j
#     flag = 1
#     while i < 1000:
#         num = i
#         digits = []
#         while num != 0:
#             digits.append(num%base)
#             num = num//base
#         s = sum(digits)
#         if s % j != 0:
#             flag = 0
#             break
#         i *= j
#
#     if flag:
#         res.append(j)
#
# print(*res)

#Palindrome
# s = input()
# m = len(s)//2
# if len(s) % 2 :
#     flag = 1
# else:
#     flag = 0
#
# while m < len(s):
#     res = 1
#     if flag:
#         right = m + 1
#         left = m - 1
#     else:
#         right = m
#         left = m - 1
#     while right < len(s) and right >= 0:
#         if s[right] == s[left]:
#             right += 1
#             left -= 1
#         else:
#             res = 0
#             break
#     if res:
#         break
#
#     if flag:
#         m += 1
#
#     flag = not flag
#
# print(len(s) + left + 1)

#답지
# s = input()
# for i in range(len(s),len(s)*2):
#     flag = True
#     for j in range(len(s)):
#         if i - j -1 < len(s) and s[i-j-1] != s[j]:
#             flag = False
#             break
#     if flag :
#         break
# print(i)

#FriendScore
# x = list(input())
# friends = [x]
# n = len(x)
# m = 0
# for _ in range(n-1):
#     friends.append(list(input()))
#
# for i in range(n):
#     s = 0
#     li = [0]*n
#     li[i] = 1
#     for j in range(n):
#         if friends[i][j] == 'Y' and li[j] == 0:
#             li[j] = 1
#             s += 1
#             for k in range(n):
#                 if friends[j][k] == 'Y' and li[k] == 0:
#                     li[k] = 1
#                     s += 1
#     m = max(m, s)
# print(m)
# NNNNNNNNNNNNNNY
# NNNNNNNNNNNNNNN
# NNNNNNNYNNNNNNN
# NNNNNNNYNNNNNNY
# NNNNNNNNNNNNNNY
# NNNNNNNNYNNNNNN
# NNNNNNNNNNNNNNN
# NNYYNNNNNNNNNNN
# NNNNNYNNNNNYNNN
# NNNNNNNNNNNNNNY
# NNNNNNNNNNNNNNN
# NNNNNNNNYNNNNNN
# NNNNNNNNNNNNNNN
# NNNNNNNNNNNNNNN
# YNNYYNNNNYNNNNN


