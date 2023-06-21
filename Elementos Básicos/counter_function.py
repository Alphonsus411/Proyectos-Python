"""
Fill in the blanks to complete the “counter” function. 
his function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. 
Otherwise, it should count up from “start” to “stop”. 
Complete the code so that a function call like “counter(3, 1)” 
will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.
"""
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while return_string != stop:
        # Complete the while loop
            print(return_string)
            # Add the numbers to the "return_string"
            if start > stop:
                return_string -= ","
            break
            # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while return_string != stop:
        # Complete the while loop
            print(return_string)
            # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            break
            # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"