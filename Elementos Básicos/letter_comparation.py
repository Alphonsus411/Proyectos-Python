"""
Fill in the blanks to complete the function.  
The character translator function receives a single lowercase letter, 
then prints the numeric location of the letter in the English alphabet.
For example, “a” would return 1 and “b” would return 2. 
Currently, this function only supports the letters “a”, “b”, “c”, and “d”
It returns "unknown" for all other letters or if the letter is uppercase.

"""
def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown