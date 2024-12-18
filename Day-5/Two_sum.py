# Find two numbers in an array that sum up to a target value.


def two_sum(nums,target):
    num_map = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i
    return []

nums = [2,7,11,16]
target = 9

print(two_sum(nums,target))