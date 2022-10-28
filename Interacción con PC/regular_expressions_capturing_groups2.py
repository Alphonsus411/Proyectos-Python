"""
Fix the regular expression used in the rearrange_name function 
so that it can match middle names, middle initials, as well as double surnames. 
      
"""

import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[1], result[2])

name=rearrange_name("Kennedy, John F.")
print(name)

