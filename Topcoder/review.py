class Solution:
    mi_n = 10 ** 5

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        s = sum(nums)

        for i in range(len(nums)):
            num = s
            for j in range(len(nums), i, -1):
                if (j == len(nums)):
                    pass
                else:
                    num -= nums[j]
                if (num >= target):
                    self.mi_n = min(j - i, self.mi_n)
            s -= nums[i]

        if (self.mi_n == 10 ** 5):
            return 0
        else:
            return self.mi_n


c = Solution()
t = int(input())
n = list(map(int,input().split()))
print(c.minSubArrayLen(t,n))