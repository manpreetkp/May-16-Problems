# Function that finds two numbers that add up to a specific target number
# @author Manpreet Kaur

def two_sum(nums, target):
    # For loop iterates over each element in the list 
    for i in range(len(nums)-1):
        # For loop iterates over each subsequent element in the list
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] # Returns the indices of the two numbers that equal the target

# Test
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))
