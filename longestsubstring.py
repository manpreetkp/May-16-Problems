# Function that finds the length of the longest substring without repeating characters
# @author Manpreet Kaur

def longest_substring_length(s):
    seen_indexes = {}   # Dictionary where most recent index of each character is stored
    substring = 0   # start index of non-repeating substring
    max_len = 0

    for i in range(len(s)):
        char = s[i]
        if char in seen_indexes:
            if seen_indexes[char] >= substring:
                substring = seen_indexes[char] + 1  # Move the start of the substring to after the character that is passing the previous if statements
        seen_indexes[char] = i  # updates last seen index of the character
        curr_len = i - substring + 1    # calculates current length of subtring
        if curr_len > max_len:
            max_len = curr_len
    return max_len

# Test             
s = "abcabcbb"
print(longest_substring_length(s))
