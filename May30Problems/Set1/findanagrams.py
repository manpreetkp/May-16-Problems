# Function that finds all the start indices of the a non-empty string p's anagrams in string s
# @author Manpreet Kaur

def find_all_anagrams(s,p):

    char_to_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    p_char_count = [0] * 26     # Array to count frequency of characters in string p
    s_char_count = [0] * 26     # Array to count frequency of characters in string s
    
    result_indices = [0] * len(s)
    result_counter = 0

    # Complete the array for string p
    for char in p:
        p_char_count[char_to_index[char]] += 1
    
    # Array to count frequency of characters in substring of s
    for char in s[:len(p)]:
        s_char_count[char_to_index[char]] += 1
    
    # If the counts match for the first substring then it becomes the first result
    if s_char_count == p_char_count:
        result_indices[result_counter] = 0
        result_counter += 1
    
    # Continues to check over different substrings of s to check and update for anagrams
    for i in range(1, len(s) - len(p) + 1):
        old_char_count = s[i-1]
        new_char_count = s[i + len(p) - 1]

        s_char_count[char_to_index[old_char_count]] -= 1
        s_char_count[char_to_index[new_char_count]] += 1

        if s_char_count == p_char_count:
            result_indices[result_counter] = i
            result_counter += 1
        
    return result_indices[:result_counter]

# Test
s = "cbaebabacd"
p = "abc"
print(find_all_anagrams(s, p))
