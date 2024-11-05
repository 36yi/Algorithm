class ThePalindrome:
    # 내가 만든겨
    # def find(self, word):
    #     length = len(word)
    #     start = length // 2
    #
    #     while start < length:
    #         left = start - 1
    #         if word[start] == word[start - 1]:
    #             right = start
    #         else:
    #             right = start + 1
    #
    #         flag = 1
    #
    #         while right < length:
    #             if(word[left] != word[right]):
    #                 flag = 0
    #                 break
    #             left -= 1
    #             right += 1
    #
    #         if(flag):
    #             return length + left + 1
    #
    #         start += 1
    #
    #     return length * 2

    #   답지 풀이 지렸다
    def find(self,word):
        i = len(word)
        while(True):
            flag = 1
            for j in range(len(word)):
                if (i-1-j) < len(word) and (word[j] != word[i-1-j]):
                    flag = 0
                    break
            if (flag): return i
            else: i += 1

c = ThePalindrome()
s = input("s = ")
print("Returns: ",c.find(s))