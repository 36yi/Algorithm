class InterestingDigits:
    def s(self, base, n):
        su_m = 0
        length = 1
        li = []
        while base ** length <= n:
            length += 1

        for i in range(length-1,-1,-1):
            li.append(n // (base ** i))
            su_m += n // (base ** i)
            n %= base ** i

        return su_m


    def digits(self, base):
        li= []
        for i in range(2,base):
            j = 1
            flag = 1
            num = i*j
            while num < 1000:
                digits_sum = self.s(base,num)
                if digits_sum % i != 0:
                    flag = 0
                    break
                j += 1
                num = i*j
            if flag:
                li.append(i)

        return li


b = int(input("base = "))
c = InterestingDigits()
print(c.digits(b))

