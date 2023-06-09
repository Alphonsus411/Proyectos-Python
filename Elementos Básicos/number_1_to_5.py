#  Find and correct the error in the for loop below.  
# The loop should check each number from 1 to 5 and identify if the number is odd or even.  

for number in range(5):
    if number % 2 == 0:
        print("odd")
    else:
        print("even")
        
# Should print:
# odd
# even
# odd
# even
# odd