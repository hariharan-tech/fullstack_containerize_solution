## Topic : JSON
# Exercise 001

""" 
Problem Statement : 
Read the Employee.json from the file and print the employee details.

Approach :
Complete the following program and make sure the test cases in TestLab001.py passes successfully/

"""


import json
from os import read


def readEmployeeFromJSONFile():
    # Write code to open the file
    data = open("Employee.json")
    employee_data = json.load(data)
    data.close()

    # Load json data as python object.
    # hint : explore json library

    return employee_data