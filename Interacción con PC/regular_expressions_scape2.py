"""
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
 (including letters, numbers, and underscores) separated by one or more whitespace characters.
"""

import re


def check_character_groups(text):
    result = re.search(r"\w+\s\w+", text)


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False
