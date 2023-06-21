"""
Consider the following scenario about using Python lists: 

A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students in the order they arrived in the classroom. 
Aniyah was the first one to note which students arrived, and then Imani took over. 
After class, they each entered their lists into the computer and emailed them to the professor. 
The professor wants to combine the two lists into one and sort it in alphabetical order. 

- Complete the code by combining the two lists into one and then sorting the new list. This function should:

- accept two lists through the function’s parameters;,

- combine the two lists;

- sort the combined list in alphabetical order;

return the new list. 
"""
def alphabetize_lists(list1, list2):

  # Initialize a new list.
  new_list = []
  # Combine the lists.
  new_list = list1 + list2
  # Sort the combined lists.
  new_list.sort()
  # Assign the combined lists to the "new_list".
  new_list = new_list
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
