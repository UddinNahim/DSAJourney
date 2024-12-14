# Count the occurrences of each element in an array.

def count_frequencies(arr):
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num,0) + 1
    return freq

print(count_frequencies([1, 2, 2, 3, 3, 3,3]))