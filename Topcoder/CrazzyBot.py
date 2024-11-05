# 내 답은 모든 확률이 동등한걸 가정한것 오답이긴한데 문제풀이는 비슷
# class CrazyBot():
#     cnt = 0
#     success = 0
#     def getProbability(self, n, east, west, south, north):
#         direction = []
#         if(east > 0):
#             direction.append('e')
#
#         if(west > 0):
#             direction.append('w')1
#
#         if(south > 0):
#             direction.append('s')
#
#         if(north > 0):
#             direction.append('n')
#         CrazyBot.cnt = len(direction) ** n
#         for i in direction:
#             self.moveRobot(n,1,i,[[0,0]],direction)
#
#         return CrazyBot.success/CrazyBot.cnt
#
#     def moveRobot(self,n,depth,way,footprints,way_list):
#
#         current_x = footprints[-1][0]
#         current_y = footprints[-1][1]
#         if(way == 'e'):
#             current_x += 1
#         elif(way == 'w'):
#             current_x -= 1
#         elif(way == 's'):
#             current_y -= 1
#         else:
#             current_y += 1
#         current = [current_x,current_y]
#         if(current in footprints):
#             return
#         if(n == depth):
#             CrazyBot.success += 1
#             return
#
#         else:
#             footprints.append(current)
#             for i in way_list:
#                 self.moveRobot(n,depth + 1, i, footprints, way_list)
#       ***** footprints.pop() #이거 안 써주면 footprint에 들어간 값이 다른 경우에서 적용됨 그니까 지나가지 않은 자리여도 지나간 자리가 됨

class CrazyBot():
    prob = [0] * 4
    grid = [[0]* 100 for _ in range(100)]
    vx = [1,-1,0,0]
    vy = [0,0,1,-1]
    def getProbability(self, n, east, west, south, north):
        CrazyBot.prob[0] = round(east/100,2)
        CrazyBot.prob[1] = round(west/100,2)
        CrazyBot.prob[2] = round(south/100,2)
        CrazyBot.prob[3] = round(north/100,2)
        return self.dfs(n,50,50)

    def dfs(self,n,x,y):
        if(CrazyBot.grid[x][y] == 1):
            return 0
        if(n == 0):
            return 1
        (CrazyBot.grid)[x][y] = 1
        ret = 0.0
        for i in range(4):
            ret += self.dfs(n-1,x + CrazyBot.vx[i], y + CrazyBot.vy[i]) * CrazyBot.prob[i]
        CrazyBot.grid[x][y] = 0
        return ret

c = CrazyBot()
n = int(input("n = "))
east = int(input("east = "))
west = int(input("west = "))
south = int(input("south = "))
north = int(input("north = "))
print(c.getProbability(n,east,west,south,north))


# 얇은 복사(안에 요소들은 참조만 복사됨)
# li = [[1,2,3],[4,5,6]]
# li2 = li
# li2[1][0] = 5
# print(li)
#깊은 복사는 copy라이브러리를 써서 가능
# 파이썬의 참조복사
# li = [1,2,3]
# li2 = li
# li2[0] += 1
# print(li)


####
#li = [[10] * 10] * 10 하면
#한 리스트만 바뀌어도 다 바뀜 이것도 얇은 복사