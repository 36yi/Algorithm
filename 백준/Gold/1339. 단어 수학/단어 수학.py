N = int(input())

words = [input() for _ in range(N)]
words.sort(key=lambda x: len(x))
SUM = [0] * 26
for word in words:
    for i in range(len(word)):
        index = ord(word[i]) - ord('A')
        SUM[index] += 10 ** (len(word) - i - 1)

pairs = []
for i in range(26):
    if SUM[i] > 0:
        pairs.append((i, SUM[i]))

pairs.sort(key = lambda x: x[1], reverse = True)

num = 9
answer = [0] * 26
for index, _ in pairs:
    answer[index] = num
    num -= 1

result = 0
for word in words:
    number = 0
    for i in range(len(word)-1,-1,-1):
        index = ord(word[i]) - ord('A')
        number += answer[index] * (10 ** (len(word)-i-1))

    result += number

print(result)
