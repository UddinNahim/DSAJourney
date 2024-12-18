def longest_zero_sum_subarray(arr):
    prefix_sum = 0
    hashmap = {}
    max_length = 0

    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum == 0:
            max_length = i + 1
        elif prefix_sum in hashmap:
            max_length = max(max_length, i - hashmap[prefix_sum])
        else:
            hashmap[prefix_sum] = i
    return max_length

print(longest_zero_sum_subarray([1, 2, -3, 3, 1, -4, 2, 3]))

