# 643. Maximum Average Subarray I

def max_average(nums,k):
    current_sum = maxSum = sum(nums[:k])
    for i in range(k,len(nums)):
        current_sum += nums[i] - nums[i-k]
        maxSum = max(maxSum, current_sum)
    return maxSum /k




nums = [1,12,-5,-6,50,3]
k = 4
print(max_average(nums,k))

