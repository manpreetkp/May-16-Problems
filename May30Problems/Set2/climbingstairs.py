# Function that counts the number of ways to climb to the top of teh stairs when you can climb 1 or 2 steps at a time
# @author Manpreet Kaur

def climbing_stairs(n):
    # Shows how if there is 1 step then there is only 1 way to climb
    if n == 1:
        return 1
    # Shows how if there are 2 steps then there are 2 ways to climb
    elif n == 2:
        return 2
    
    a, b = 1, 2
    # From the third step to the nth step, calculates the number of ways to climb the stairs
    for i in range(2, n):
        a, b = b, a+b
    return b

# Test
n = 3
print(climbing_stairs(n))
