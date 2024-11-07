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

#CrazyBot
# n = int(input())
# move_x = [-1,1,0,0]
# move_y = [0,0,-1,1]
# prob_list = []
# for _ in range(4):
#     prob_list.append(int(input()) * 0.01)
# trail = set()
# def move(cnt,index_x,index_y):
#     if cnt > n:
#         return 1
#
#     if (index_x,index_y) in trail:
#         return 0
#
#     trail.add((index_x,index_y))
#     prob = 0
#     for i in range(4):
#         prob += move(cnt+1,index_x+move_x[i],index_y+move_y[i]) * prob_list[i]
#
#     trail.remove((index_x,index_y))
#     return prob
#
# print(move(0,0,0))
##set에는 mutable타입이 들어갈 수 없다

#MazeMaker
# maze = list(input().split(", "))
# startRow = int(input())
# startCol = int(input())
# moveRow = list(map(int,input().split()))
# moveCol = list(map(int,input().split()))
#
# grid=[]
# row = len(maze)
# col = len(maze[0])
#
# for i in range(row):
#     li = []
#     for j in range(col):
#         if maze[i][j] == ".":
#             li.append(0)
#         else:
#             li.append(-1)
#     grid.append(li)
# def check(cnt, index_row, index_col):
#     if not (0 <= index_row < row and 0 <= index_col < col):
#         return
#     if grid[index_row][index_col] == -1:
#         return
#
#     if grid[index_row][index_col] != 0:
#         if grid[index_row][index_col] <= cnt:
#             return
#
#     grid[index_row][index_col] = cnt
#
#     for i in range(len(moveRow)):
#         check(cnt + 1, index_row + moveRow[i], index_col + moveCol[i])
#
#     return
#
# check(0,startRow,startCol)
#
# m = 0
# flag = 1
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == 0:
#             if i == startRow and j == startCol:
#                 continue
#             print(-1)
#             flag = 0
#             break
#
#         if grid[i][j] > m:
#             m = grid[i][j]
#
# if flag:
#     print(m)

#dfs로 풀었는디 dfs는 내가 최대깊이까지 판 루트 보다 다른 루트에 최단거리가 있을 수 있음 ---> bfs는 그럴일 이 없다 ( 가지치기에 더 적합)

# bfs
# from collections import deque
#
# maze = list(input().split(", "))
# startRow = int(input())
# startCol = int(input())
# moveRow = list(map(int,input().split()))
# moveCol = list(map(int,input().split()))
#
# grid=[]
# row = len(maze)
# col = len(maze[0])
#
# for i in range(row):
#     li = []
#     for j in range(col):
#         if maze[i][j] == ".":
#             li.append(0)
#         else:
#             li.append(-1)
#     grid.append(li)
#
# queue = deque([(startRow,startCol)])
# while queue:
#     current = queue.popleft()
#     cnt = grid[current[0]][current[1]]
#
#     for i in range(len(moveRow)):
#         index_row = current[0] + moveRow[i]
#         index_col = current[1] + moveCol[i]
#
#         if not(0 <= index_row < len(grid) and 0 <= index_col < len(grid[0])):
#             continue
#
#         if grid[index_row][index_col] == 0:
#             queue.append((index_row,index_col))
#             grid[index_row][index_col] = cnt+1
#
# m = 0
# flag = 1
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == 0:
#             if i == startRow and j == startCol:
#                 continue
#             print(-1)
#             flag = 0
#             break
#
#         if grid[i][j] > m:
#             m = grid[i][j]
#
# if flag:
#     print(m)

#NumberMagicEasy
# numset = {i for i in range(1,17)}
# s = input()
# card = {0:{1,2,3,4,5,6,7,8}, 1:{1,2,3,4,9,10,11,12}, 2:{1,2,5,6,9,10,13,14}, 3:{1,3,5,7,9,11,13,15}}
# for i in range(len(s)):
#     if s[i] == 'N':
#         numset = numset - card[i]
#
#     else:
#         numset = numset & card[i]
#
# print(numset)
# 답지 풀이
# def check(li, number):
#     for num in li:
#         if (num == number):
#             return 'Y'
#
#     return 'N'
#
# card1 = [1,2,3,4,5,6,7,8]
# card2 = [1,2,3,4,9,10,11,12]
# card3 = [1,2,5,6,9,10,13,14]
# card4 = [1,3,5,7,9,11,13,15]
#
# s = input()
#
# for i in range(1,17):
#     if check(card1,i) != s[0]:
#         continue
#     if check(card2,i) != s[1]:
#         continue
#     if check(card3,i) != s[2]:
#         continue
#     if check(card4,i) != s[3]:
#         continue
#     print(i)
#     break

#두번쨰 답지

# s = ["YYYYYYYYNNNNNNNN",
#     "YYYYNNNNYYYYNNNN",
#     "YYNNYYNNYYNNYYNN",
#     "YNYNYNYNYNYNYNYN"]
#
# ans = input()
# for i in range(16):
#     tmp = s[0][i] + s[1][i] + s[2][i] + s[3][i]
#     if(tmp == ans):
#         print(i+1)
#         break

#세번째 풀이는 모든 숫자와 문자열 매칭한 크기가 16인 리스트
# ex) ["YYYY","YYYN","YYNY",..."NNNN"] 정답인거 찾기
