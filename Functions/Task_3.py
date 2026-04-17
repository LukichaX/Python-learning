def average(nums):
    if len(nums) == 0:
        return 0
    else:
        return sum(nums) / len(nums)

print(average([1, 2, 3, 4, 5]))