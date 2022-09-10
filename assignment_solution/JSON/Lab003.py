## Topic : JSON
# Exercise 003

""" 
Problem Statement : 
Read the Employee.json from the file and print the employee details.
Try to add another attributes
1)   "manager" with any String value
2)   "yearsofexp" with any integer value


Approach :
Complete the following program and make sure the test cases in TestLab003.py passes successfully/

"""


import json


def readEmployeeFromJSONFile():
    # Write code to open the file
    json_data = open("Employee.json")
    # Load json data as python object.
    employee_data = json.load(json_data)
    json_data.close()
    # hint : explore json library
    
    # update dictionary to have new attributes
    employee_data["manager"] = "Alice"
    employee_data["yearsofexp"] = 5
    return employee_data