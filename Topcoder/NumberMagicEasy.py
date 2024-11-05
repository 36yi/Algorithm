class NumberMagicEasy():
    # 내 풀이
    # 간결 , 직관 근데 리스트 삭제 가 많아지면 성능 저하
    # def theNumber(self, answer):

        # wrong = set()
        # right = []
        # card = [ [1,2,3,4,5,6,7,8],
        #          [1,2,3,4,9,10,11,12],
        #          [1,2,5,6,9,10,13,14],
        #          [1,3,5,7,9,11,13,15] ]
        #
        # for i in range(4):
        #     print(right,wrong)
        #     if answer[i] == 'N':
        #         for j in range(8):
        #             if card[i][j] in right:
        #                 right.remove(card[i][j])
        #                 wrong.add(card[i][j])
        #
        #             elif card[i][j] not in wrong:
        #                 wrong.add(card[i][j])
        #
        #     else:
        #         li =set()
        #         for j in range(8):
        #             if card[i][j] not in wrong:
        #                 if card[i][j] not in right:
        #                     right.append(card[i][j])
        #                 else:
        #                     li.add(card[i][j])
        #
        #
        #         if li :
        #
        #             right = list(li)
        #
        # print(right,wrong)
        # if right:
        #     return right[0]
        # else:
        #     return 16


    # 답지 풀이 1
    # 일단 answer와 숫자가 1ㄷ1 대응하는 것을 응용
    # 각 숫자마다 카드별로 내는 답이 answer랑 일치하는지 확인
    # def check(self, li, num):
    #     for i in li:
    #         if i == num:
    #             return 'Y'
    #     return 'N'
    #
    # def theNumber(self,answer):
    #     card_1 = [1,2,3,4,5,6,7,8]
    #     card_2 = [1,2,3,4,9,10,11,12]
    #     card_3 = [1,2,5,6,9,10,13,14]
    #     card_4 = [1,3,5,7,9,11,13,15]
    #
    #     for i in range(1,17):
    #         if self.check(card_1, i) != answer[0] : continue
    #         if self.check(card_2, i) != answer[1] : continue
    #         if self.check(card_3, i) != answer[2] : continue
    #         if self.check(card_4, i) != answer[3] : continue
    #         return i
    #     return 0

    # 답지 풀이 2

    # def theNumber(self,answer):
    #     c = ['YYYYYYYYNNNNNNNN', 'YYYYNNNNYYYYNNNN', 'YYNNYYNNYYNNYYNN','YNYNYNYNYNYNYNYN']
    #     for i in range(16):
    #         li= [c[0][i], c[1][i], c[2][i], c[3][i]]
    #         if(''.join(li)==answer):
    #             return i + 1
    #     return 0

    #답지풀이 3 bit탐색이라곤 하는데 흠 Y를 0으로 N을 1로 해서
    #사실 잘 모르겠음 트리 구조가 뭔가 이해가 될거같은데 뭔가 또 뭔가
    def theNumber(self,answer):
        c = ['YYYY',
             'YYYN',
             'YYNY',
             'YYNN',
             'YNYY',
             'YNYN',
             'YNNY',
             'YNNN',
             'NYYY',
             'NYYN',
             'NYNY',
             'NYNN',
             'NNYY',
             'NNYN',
             'NNNY',
             'NNNN',
             'NNNN']
        for i in range(16):
            if(c[i] == answer):
                return i + 1
        return 0

c = NumberMagicEasy()
print(c.theNumber("YYYN"))




