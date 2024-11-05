# **** 답지만 봄 메모이제이션 재귀 (DP의 한 종류)
class CorporationSalary():
    salaries = [0]*51
    def totalSalary(self, relations):
        total = 0
        for i in range(len(relations)):
            total += self.getSalary(i,  relations)

        return total

    def getSalary(self, index, relations):
        if(self.salaries[index] == 0):
            salary = 0
            for i in range(len(relations)):

                if(relations[index][i] == 'Y'):
                    salary += self.getSalary(i, relations)

            if(salary == 0):
                salary = 1

            self.salaries[index] = salary

        return self.salaries[index]


c = CorporationSalary()
li = list(input("relations = ").split())
print(li)
print(c.totalSalary(li))

