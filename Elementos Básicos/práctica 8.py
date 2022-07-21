def even_numbers(maximum):
    return_string = ""
    for x in range(0, maximum + 1, 2):
        return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # should be "2 4 6"
print(even_numbers(10))  # should be "2 4 6 8 10"
print(even_numbers(1))  # should be ""
print(even_numbers(3))  # should be "2"
print(even_numbers(0))  # should be ""
