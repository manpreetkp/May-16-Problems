# Function that finds the contiguous subarray which has the largest sum and return its sum
# @author Manpreet Kaur

def max_subarr(nums):
    largest_sum = nums[0]

    for i in range(1, len(nums)):
        # If the previous element is positive then add it to the current element
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        #Compare elements and update the largest_sum if the current element is larger
        if nums[i] > largest_sum:
            largest_sum = nums[i]

    return largest_sum

# Test
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarr(nums))
