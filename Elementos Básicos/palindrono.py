def is_palindrone(input_string):
    #We´ll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    #Traverse through each letter of the input string
    for letter in input_string:
        #Add any non-blank letters to the
        #end of one string, and to the front
        #of the other string.
        if letter != " ":
            new_string = new_string + letter.lower()
            reverse_string = letter.lower() + reverse_string
             
    #Compare the strings
    if new_string == reverse_string:
        return True
    return False

print(is_palindrone("Never Odd or Even")) #Should be True
print(is_palindrone("abc")) #Should be False
print(is_palindrone("kayak")) #Should be True