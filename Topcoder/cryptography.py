class Cryptography:
    def encrypt(self, numbers):
        m = 0
        for i in range(len(numbers)):
            s = numbers[i] + 1
            for j in range(len(numbers)):
                if(i == j):
                    continue
                else:
                    s *= numbers[j]
            if(m < s):
                m = s

        return m

c = Cryptography()
li = list(map(int,input("numbers: ").split(", ")))
print(c.encrypt(li))