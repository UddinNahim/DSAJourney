def two_sum(arr,target):
    hashmap = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return None

print(two_sum([2,7,11,15], 9))