# Fill in the blanks to complete the “even_numbers” function. 
# This function should return a space-separated string of all positive even numbers, 
# excluding 0, up to and including the “maximum” variable that's passed into the function. 
# Complete the for loop so that a function call like “even_numbers(6)” will return the numbers “2 4 6”.  



def even_numbers(maximum):

    return_string = "" # Initializes variable as a string
    maximun += 1 # Adds 1 to the maximum value

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for number in range(2, maximum, 2):

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string += str(number) + " "

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed