# Reverse an array.

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left +=1 
        right -=1
    return arr
        




arr = [1,2,3,5,6,7]
print( reverse_array(arr))