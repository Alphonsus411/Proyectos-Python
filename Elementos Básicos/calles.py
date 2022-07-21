def format_address(address_string):
    # Declare variables
    house_number = street_name = city = state = zip_code = None
    # Separate the address string into parts
    address_parts = address_string.split(',')
    # Traverse through the address parts
    for part in address_parts:
        # Remove leading and trailing whitespace
        part = part.strip()
        # Separate the part into 2 parts: number and name
        part_parts = part.split()
        # Check if the first part is a house number
        if part_parts[0].isdigit():
            # Assign it to the house number variable
            house_number = part_parts[0]
        else:
            # It must be a street name
            # Append the first part to the street name variable
            if street_name == None:
                street_name = part_parts[0]
            else:
                street_name += ' ' + part_parts[0]
    # Return the formatted string
    return "house number {} on street named {} in {}".format(house_number, street_name, city)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
