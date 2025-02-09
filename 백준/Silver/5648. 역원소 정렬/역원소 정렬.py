nums = []
nums += list(input().split())
l = int(nums[0])

while True:
    if len(nums) == l+1:
        break

    nums += list(input().split())

nums = nums[1:]
for i in range(l):
    nums[i]= int(nums[i][::-1])

nums.sort()

print(*nums, sep='\n')