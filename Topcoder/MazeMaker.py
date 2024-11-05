from collections import deque

class MazeMaker():
    # 내 정답
    # 나는 dfs로함 이러면 모든 노드를 돠 훑어봐야 이게 최단경로인지 확인가능함.
    # grid = []
    # vx = []
    # vy = []
    # def longestPath(self,maze,startRow,startCol,moveRow,moveCol):
    #     self.grid = [[200] * len(maze[0]) for _ in range(len(maze))]
    #     for i in range(len(moveRow)):
    #         self.vx.append(moveRow[i])
    #         self.vy.append(moveCol[i])
    #
    #     self.dfs(maze,0,startRow,startCol)
    #     m = 0
    #     for i in range(len(self.grid)):
    #         for j in range(len(self.grid[0])):
    #             if self.grid[i][j] == 200:
    #                 print(i, j)
    #                 return -1
    #             if self.grid[i][j] > m:
    #                 m = self.grid[i][j]
    #     print(self.grid)
    #     return m
    # def dfs(self,maze,walk,x,y):
    #     print(walk,x,y)
    #     if(x >= len(maze) or y >= len(maze[0])) or (x < 0 or y < 0):
    #         return
    #     if(maze[x][y] == 'X'):
    #         self.grid[x][y] = -1
    #         return
    #
    #     if(self.grid[x][y] <= walk):
    #         return
    #
    #     self.grid[x][y] = walk
    #
    #     for i in range(len(self.vx)):
    #         self.dfs(maze,walk + 1, x + self.vx[i], y + self.vy[i])

    #bfs가 더 좋음
    #각 노드에 도착했을때 그것이 최단경로임

    def longestPath(self,maze,startRow,startCol,moveRow,moveCol):
        grid = [[200] * len(maze[0]) for _ in range(len(maze))]

        Que = deque()
        visited = []
        Que.append([startRow, startCol])

        grid[startRow][startCol] = 0
        visited.append([startRow,startCol])
        while Que:
            print(list(Que))
            i, j = Que.popleft()
            for k in range(len(moveRow)):
                nx = i + moveRow[k]
                ny = j + moveCol[k]

                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                    if maze[nx][ny] == 'X':
                        visited.append([nx, ny])
                        grid[nx][ny] = -1
                        continue
                    if [nx, ny] not in visited:
                        print(nx,ny,grid[i][j] + 1)
                        Que.append([nx, ny])
                        visited.append([nx, ny])
                        grid[nx][ny] = grid[i][j] + 1

        m = 0
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 200:
                    print(i, j)
                    return -1
                if grid[i][j] > m:
                    m = grid[i][j]

        return m


c = MazeMaker()
li = list(map(list,input("maze = ").split(', ')))
sR = int(input("StartRow = "))
sC = int(input("StartCol = "))
mR = list(map(int,input("moveRow = ").split(', ')))
mC = list(map(int,input("moveCol = ").split(', ')))
print(c.longestPath(li,sR,sC,mR,mC))


