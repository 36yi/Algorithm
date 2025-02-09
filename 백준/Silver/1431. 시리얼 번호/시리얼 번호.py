def func(x):
    s = 0
    for i in range(len(x)):
        if x[i].isdigit():
            s += int(x[i])

    return s

n = int(input())
words = []

for _ in range(n):
    words.append(input())

words.sort()
words.sort(key = lambda x : func(x))
words.sort(key = lambda x : len(x))

print(*words,sep='\n')



