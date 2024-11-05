class FriendScore:
    def highestScore(self, array):
        # 내 풀이
        # m = 0
        # num = len(array)
        # for i in range(num):
        #     li = []
        #     s = array[i]
        #     for j in range(num):
        #         if(s[j] == "Y"):
        #             if j not in li:
        #                 li.append(j)
        #             s2 = array[j]
        #             for k in range(num):
        #                 if(s2[k] == "Y" and k not in li):
        #                     li.append(k)
        #
        #     if(len(li) - 1 > m):
        #         m = len(li) - 1
        #         print(i,li)
        #
        # return m

        # 답지 풀이도 비슷한데 뭔가 구조가 더 단순? 좀더 깔끔하다

        m = 0
        num = len(array)
        for i in range(num):
            cnt = 0

            for j in range(num):
                if(i == j): #자기 자신은 고려하지 않는다
                    continue
                if array[i][j] == 'Y': #직접 친구면 바로 count
                    cnt += 1

                else: #직접 친구가 아닌데 친구가 되는경우는 공통된 친구가 있는지 확인하는 것
                    for k in range(num):
                        if array[j][k] == 'Y' and array[i][k] == 'Y':
                            cnt += 1
                            break
                m = max(m, cnt)

        return m








c = FriendScore()
arr = list(input("friends = ").split())
print(c.highestScore(arr))