"""
Fill in the blanks to complete the “odd_numbers” function. 
This function should return a space-separated string of all odd positive numbers, 
up to and including the “maximum” variable that's passed into the function. 
Complete the for loop so that a function call like “odd_numbers(6)” will return the numbers “1 3 5”.
"""

def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string
    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for number in range(1, maximum + 1, 2):

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        return_string += str(number) + " "

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed