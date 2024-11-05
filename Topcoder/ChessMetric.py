class ChessMetric():
    dx = [-1,-1,-1,0,0,1,1,1,-2,-2,-1,1,-1,1,2,2]
    dy = [1,0,-1,1,-1,1,0,-1,1,-1,2,2,-2,-2,1,-1]
    dp = [[[0] * 55 for i in range(100)] for j in range(100)] # for for 사이에 중괄호 안해주면  그냥 10000개 2차원 배열

    def howMany(self, size, start, end, numMoves):
        # 일단 다 답지 봤다.
        # 아니 이게 이렇게 간단하게 푸네
        # 3차원 dp는 어케생각했노
        # 이동하는 경우일떄 이 방법이 개날먹임

        self.dp[start[1]][start[0]][0] = 1
        for i in range(1,numMoves+1):
            for x in range(size):
                for y in range(size):
                    for j in range(16):
                        nx = x + self.dx[j]
                        ny = y + self.dy[j]
                        if(0<=nx<size and 0<=ny<size):
                            self.dp[ny][nx][i] += self.dp[y][x][i-1]

        return self.dp[end[1]][end[0]][numMoves]

c = ChessMetric()
s = int(input("size = "))
start = list(map(int,input("start = ").split()))
end = list(map(int,input("end = ").split()))
numMoves = int(input("numMoves = "))
print(c.howMany(s,start,end,numMoves))
