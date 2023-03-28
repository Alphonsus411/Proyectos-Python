"""
Fill in the blanks to complete the function. The “make_positive” function takes in a number and converts that number to its positive equivalent.  
Complete the function to accomplish the following tasks:

- use an if statement to test if the number is negative;

- use a calculation inside the if statement to change the negative number to be positive;

- use a calculation in the else statement to return any positive “number” unchanged.
"""

def make_positive(number):
    if number < 0:
        result = number * -1
    else:
        result = number
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25)) # Should print 0.25
print(make_positive(5))    # Should print 5
