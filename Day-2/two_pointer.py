#checking if two numbers in a a sorted array sum to a target

def two_pointer(arr,target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left,right]
        elif current_sum < target:
            left +=1
        else:
            right -= 1
    return None
print(two_pointer([1,2,3,5,6,7],8))
