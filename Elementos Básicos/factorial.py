""" Fill in the blanks to complete the “factorial” function. This function will accept an integer variable “n” through the function parameters and produce the factorials of this number (by multiplying this value by every number less than the original number [n*(n-1)], excluding 0).  To do this, the function should:

accept an integer variable “n” through the function parameters;

initialize a variable “result” to the value of the “n” variable;

iterate over the values of “n” using a while loop until “n” is equal to 0;

starting at n-1, multiply the result by the current “n” value;

decrement “n” by -1.

 For example, factorial 3 would return the value of 3*2*1, which would be 6.
 """
 
def factorial(n):
    result = 1
    start = n
    n -= 1
    while n > 0 and start > 0:
        # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1
        # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1