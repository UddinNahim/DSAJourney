# Find the maximum sum of a subarray of size k.
def max_sum_subArray(arr,k):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max,window_sum)
        window_sum -= arr[i-(k-1)]
    return max_sum



output = max_sum_subArray([2,1,5,1,3,2],3)
print(output)