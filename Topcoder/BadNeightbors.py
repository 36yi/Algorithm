
class BadNeightbors():
    def maxDonations(self,donations):
        #답지 풀이 흠 이건 안에서 중복이 있지 않나
        ans = 0
        n = len(donations)
        dp = [0] * n
        for i in range(n-1):
            dp[i] = donations[i]
            if(i>0):
                dp[i] = max(dp[i],dp[i-1]) #이건 1일떄만 아닌가??
            if(i>1):
                dp[i] = max(dp[i],dp[i-2] + donations[i])
                ans = max(ans,dp[i])

        for i in range(n-1):
            dp[i] = donations[i+1]
            if(i>0):
                dp[i] = max(dp[i],dp[i-1]) #이건 1일떄만 아닌가??
            if(i>1):
                dp[i] = max(dp[i],dp[i-2] + donations[i+1])
                ans = max(ans,dp[i])
        return ans

        #나는 처음집과 마지막집이 겹치면 안된다는 걸 꺠달았을떄
        # 처음 집이 들어가는 경우를 따로 세자 라고 했는데
        # 애는 처음집을 아예배제하는경우를 새로 만들고 두개를 비교했다
        # => 나는 o(n**2) 얘는 o(2n)이렇게 됨
        # 그리고 이떄 나는 마지막 집이 들어가는 경우를 다 뺴버리는 판단을 하고
        # 첫번쨰집이 빠졌을떄가 더 이득인 경우를 생각못함



        # 내풀이는 예외처리 두개 놓침
        # 맨 처음집과 맨 마지막집이 둘 다 선택 되면 안됨
        # 맨 처음집을 포기하고 마지막집을 넣는 경우가 더 큰 경우도 생각
        # dp = [0] * len(donations)
        # zero_list = [0]
        # dp[0] = donations[0]
        # if(donations[0] > donations[1]):
        #     zero_list.append(1)
        #     dp[1] = dp[0]
        # else:
        #     dp[1] = donations[1]
        # for i in range(2, len(donations)):
        #     if(dp[i-1] > donations[i] + dp[i-2]):
        #         if(i-1 in zero_list):
        #             zero_list.append(i)
        #         dp[i] = dp[i-1]
        #     else:
        #         if(i-2 in zero_list):
        #             zero_list.append(i)
        #         dp[i] = donations[i] + dp[i-2]
        # print(zero_list)
        # print(dp)
        # if(len(dp) - 1 in zero_list):
        #     if(dp[-2] < dp[-1] - dp[0]):
        #         return dp[-1] - dp [0]
        #     else:
        #         return dp[-2]
        # else:
        #     return dp[-1]

c = BadNeightbors()
li = list(map(int,input("donations = ").split()))
print(c.maxDonations(li))
