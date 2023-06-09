# Implement the sum_positive_numbers function, as a recursive function 
# that returns the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, 
# and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  return n + sum_positive_numbers(n-1) if n > 0 else 0

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15