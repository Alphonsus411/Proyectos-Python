"""
The goal of the script is to read the CSV file and generate a report with the total number of people in each department. 
To achieve this, we will divide the script into three functions.

Let's start with the first function: read_employees(). 
This function receives a CSV file as a parameter and returns a list of dictionaries from that file. For this, we will use the CSV module.

The CSV module uses classes to read and write tabular data in CSV format. 
The CSV library allows us to both read from and write to CSV files.

Now, import the CSV module.

import csv

Define the function read_employees. This function takes file_location (path to employees.csv) as a parameter.

def read_employees(csv_file_location):

Open the CSV file by calling open and then csv.DictReader.

DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), 
but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, 
he values in the first row of the CSV file will be used as the keys. So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.

We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, 
so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. 
Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.

Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. 
We will now register a dialect empDialect.

  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.

The function will look similar to:

  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  
You now need to iterate over the CSV file that you opened, i.e., employee_file. 
When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).

Append the dictionaries to an empty initialised list employee_list as you iterate over the CSV file.

  employee_list = []
  for data in employee_file:
    employee_list.append(data)

Now return this list.

  return employee_list
Se copió correctamente
To test the function, call the function and save it to a variable called employee_list. 
Pass the path to employees.csv as a parameter to the function. Print the variable employee_list to check whether it returns a list of dictionaries.

employee_list = read_employees('<file_location>')
print(employee_list)

Replace <file_location> with the path to the employees.csv (this should look similar to the path /home/<username>/data/employees.csv). 
Replace <username> with the one mentioned in Connection Details Panel at left hand side.

Run the script. You should see a list of dictionaries printed on the screen."""

#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('<file_location>')
print(employee_list)

"""Output:
[{'Name': 'John Smith', 'Department': 'Accounting', 'Address': '121 Accounting Lane'}, 
{'Name': 'Erica Meyers', 'Department': 'IT', 'Address': '23  IT Road'},
{'Name': 'Adam Wilde', 'Department': 'IT', 'Address': '121 IT Boulevard'}, 
{'Name': 'Elizabeth Looney', 'Department': 'HR', 'Address': '67 HR Avenue'}, 
{'Name': 'Juan  Espinal', 'Department': 'Accounting', 'Address': '77 Accounting Street'}]"""


