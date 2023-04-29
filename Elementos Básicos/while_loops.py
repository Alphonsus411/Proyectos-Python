"""
The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. 
To solve the problem, you will need to:  

- Find the error in the code

- Fix the while loop so there is an exit condition

- Hint: Try running your function with the number 0 as the input and observe the result. 
"""

def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  else:
    return False
  

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False