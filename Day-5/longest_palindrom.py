# Find the longest palindrome that can be built with the letters of a given string.


def longest_palindrome(s):
    from collections import Counter
    freq = Counter(s)
    length = 0
    odd_found = False

    for count in freq.values():
        length += count // 2 * 2
        if count % 2 == 1:
            odd_found = True
    return length + 1 if odd_found else length


s = "abccccdd"
print(longest_palindrome(s))
