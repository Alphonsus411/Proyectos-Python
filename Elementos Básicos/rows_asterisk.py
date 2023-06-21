"""
Fill in the blanks to complete the “rows_asterisks” function. 
This function should print rows of asterisks (*), where the number of rows is equal to the “rows” variable. 
The number of asterisks per row should correspond to the row number 
(row 1 should have 1 asterisk, row 2 should have 2 asterisks, etc.). Complete the code so that “row_asterisks(5)” will print:
"""

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows):
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x + 1):
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above