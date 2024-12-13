# Find pairs with a given sum.
def find_pairs(arr,target):
    pairs = []
    left,right=0, len(arr) -1
    while left < right :
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return pairs

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10

print(find_pairs(arr, target))