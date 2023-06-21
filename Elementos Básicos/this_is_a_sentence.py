"""
Complete the function so that input like "This is a sentence." will return a dictionary 
that holds the count of each letter that occurs in the string: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:

accept a string “text” variable through the function’s parameters;

iterate over each character the input string to count the frequency of each letter found, (only letters should be counted, do not count blank spaces, numbers, or punctuation; keep in mind that Python is case sensitive);

populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;

return the new dictionary.
"""

def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for character in text.lower():
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if character.isalpha(): 
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if character not in dictionary: 
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
              dictionary[character] = 0
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
              dictionary[character] += 1
              letter_counter = character.counter()
      # Increment the letter counter. 
    letter_counter += 1
    # Return the dictionary.
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}