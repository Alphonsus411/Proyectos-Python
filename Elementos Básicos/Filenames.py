filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for i in filenames:
    if i == "program.c":
        newfilenames.append("program.c")
    elif i == "program.hpp":
        newfilenames.append("program.hpp")
    elif i == "stdio.hpp":
        newfilenames.append("stdio.hpp")
    elif i == "sample.hpp":
        newfilenames.append("sample.hpp")
    elif i == "a.out":
        newfilenames.append("a.out")
    elif i == "math.hpp":
        newfilenames.append("math.hpp")
    elif i == "hpp.out":
        newfilenames.append("hpp.out")
    else:
        print(i)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
