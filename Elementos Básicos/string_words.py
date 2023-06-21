"""
Fill in the blank to complete the “string_words” function. 
This function should split up the words in the given “string” and return the number of words in the “string”.  
Complete the string operation and method needed in this function 
so that a function call like "string_words("Hello, World")" will return the output "2".
"""

def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4