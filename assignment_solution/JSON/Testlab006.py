import unittest
from Lab006 import readEmployeeFromJSONFile


class TestLab006(unittest.TestCase):
    def test_Employee(self):
        employee_data = readEmployeeFromJSONFile()
        print(employee_data.name)
        print(type(employee_data))
        # add for other fields also


if __name__ == '__main__':
    unittest.main()