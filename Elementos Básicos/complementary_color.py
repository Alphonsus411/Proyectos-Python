"""
Fill in the blanks to complete the function. 
The “complementary_color” function receives a primary color name in all lower case, then prints its complementary color. 
Currently, the function only supports the primary colors of red, yellow, and blue. 
It returns "unknown" for all other colors or if the word has any uppercase characters.
"""

def complementary_color(color):
    if color == "red":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "blue":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementary_color("blue")) # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red")) # Should print green
print(complementary_color("black")) # Should print unknown
print(complementary_color("Blue")) # Should print unknown
print(complementary_color("")) # Should print unknown