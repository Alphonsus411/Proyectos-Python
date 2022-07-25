def skip_elements(elements):
    # initialize variables
    new_list = []
    i = 0

    # iterate through the list
    for i in range(len(elements)):
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # add this element to the resulting list
            new_list.append(elements[i])
        # increment i
        i += 1

    # return the resulting list
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # should return ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]))  # should return ['Orange', 'Blue', 'Purple']
print(skip_elements([""]))  # should return []
