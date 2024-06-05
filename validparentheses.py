# Function that checks if every opening bracket has a corresponding closing bracket and that they are in a correct nested order
# @author Manpreet Kaur

def valid_parentheses(s):
    string = [0] * len(s)  
    ptr = -1  
    matching_bracket = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # Check if the character is an opening bracket and if it is then account for the opening bracket
        if char in "([{":
            ptr += 1 
            string[ptr] = char  
        # Check if the character is a closing bracket
        elif char in matching_bracket:
            # If there is an empty stack or the pointer and brakcet possibilities do not match then return false
            if ptr == -1 or string[ptr] != matching_bracket[char]:
                return False
            ptr -= 1    # Move pointer down
        else:
            continue

    return ptr == -1  

# Test
s = "({[]})"
print(valid_parentheses(s)) 

