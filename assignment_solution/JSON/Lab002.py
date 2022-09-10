## Topic : JSON
# Exercise 002

""" 
Problem Statement : 
Read the student dictionary as a json string and print the student details.

Approach :
Complete the following program and make sure the test cases in TestLab002.py passes successfully.

"""
import json

student_dict = {'name': 'Gil', 'age': 20,
                'subjects': ['IT', 'OOPS', 'MATHS', 'DS']}


def getStudentDataAsJson():
    # Read the dictionary as String into student_data_json variable.

    # json.dumps() is to convert dictionary to json object
    # json.dump() is to dump/write the json object in json file

    student_data_json = json.dumps(student_dict)
    return student_data_json