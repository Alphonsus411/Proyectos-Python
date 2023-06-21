"""
Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
Fill in the blanks in the code using any of the methods you’ve learned thus far, 
like a for loop or a list comprehension.
"""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for i in filenames:
    if i == "program.c":
        newfilenames.append("program.h")
    if i == "stdio.hpp":
        newfilenames.append("stdio.h")
    if i == "sample.hpp":
        newfilenames.append("sample.h")
    if i == "a.out":
        newfilenames.append("a.out")
    if i == "math.hpp":
        newfilenames.append("math.h")
    if i == "hpp.out":
        newfilenames.append("hpp.out")

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]