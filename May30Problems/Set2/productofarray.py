# Function that returns an array of the same size where each element is the sum of all the integers in the original array except the integer at that index
# @author Manpreet Kaur

def product_arr_except_self(nums):
    size = len(nums)
    output_arr = [1] * size

    # Calculates products of all elements to the left of each element
    left_product = 1
    for i in range(size):
        output_arr[i] = left_product
        left_product *= nums[i]
    
    # Calculates products of all elements to the right of each element
    right_product = 1
    for i in range(size - 1, -1, -1):
        output_arr[i] *= right_product
        right_product *= nums[i]

    return output_arr

# Test
nums = [1, 2, 3, 4]
print(product_arr_except_self(nums))
