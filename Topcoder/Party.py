class InterestingParty():
    def BestInvitation(self, first,second):
        # 1번
        # m = 0
        # for i in range(len(first)):
        #     topic = first[i]
        #     s = first.count(topic)
        #     s += second.count(topic)
        #     if(s > m):
        #         m = s
        # for i in range(len(first)):
        #     topic = second[i]
        #     s = first.count(topic)
        #     s += second.count(topic)
        #     if(s > m):
        #         m = s
        #
        # return m

        #2 연관배열이 딕셔너리 였으
        dic = {}
        for i in range(len(first)):
            dic[first[i]] = 0
            dic[second[i]] = 0

        for i in range(len(first)):
            dic[first[i]] += 1
            dic[second[i]] += 1
        return max(dic.values())
# split(",")로 하니까 저장될때 " abc" " def" 로 됨
# 근데 그러면 어떻게 3이 나왔지? 아 " fishing"을 찾으니까 4개가 나옴
# split(", ") 이렇게 ㄱㄱ

f = list(input("first = ").split(", "))
se = list(input("second = ").split(", "))
c = InterestingParty()
print(c.BestInvitation(f,se))