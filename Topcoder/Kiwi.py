class KiwiJuiceEasy:
    def thePouring(self,capacities,bottles,fromId,toId):
        for i in range(len(fromId)):
            # 1
            # if (bottles[fromId[i]] + bottles[toId[i]] > capacities[toId[i]]):
            #     bottles[fromId[i]] = bottles[fromId[i]] + bottles[toId[i]] - capacities[toId[i]]
            #     bottles[toId[i]] = capacities[toId[i]]
            #
            #
            # else:
            #     bottles[toId[i]] = bottles[toId[i]] + bottles[fromId[i]]
            #     bottles[fromId[i]] = 0

            # 2
            # 결국 두 병에서의 변화량은 동일
            # bottles[fromId[i]]가 전부 가느냐 아니면 bottles[toId[i]]의 남은 부분만 가느냐
            # carry = min(bottles[fromId[i]],capacities[toId[i]] - bottles[toId[i]])
            # bottles[fromId[i]] -= carry
            # bottles[toId[i]] += carry

            # 3 내가 봤을 떄 이건 좀 글코 2번이 젤 좋은듯
            # fromBottle 과 toBottle의 총합은 변화가 없다.
            # 그래서 min(총합, toBottle의 용량)
            s = bottles[fromId[i]] + bottles[toId[i]]
            bottles[toId[i]] = min(s,capacities[toId[i]])
            bottles[fromId[i]] = s - bottles[toId[i]]

            #조거문은 최대한 조금 쓰래
        return bottles


a = KiwiJuiceEasy()
c = list(map(int,input("capacities = ").split(",")))
b = list(map(int,input("bottles = ").split(",")))
f = list(map(int,input("fromId = ").split(",")))
t = list(map(int,input("toId = ").split(",")))
print("Returns: ",a.thePouring(c,b,f,t))
