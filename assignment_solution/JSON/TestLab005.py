import unittest
from Lab005 import readEmployeeFromJSONFile


class TestLab005(unittest.TestCase):
    def test_Employee(self):
        employee_data = readEmployeeFromJSONFile()
        self.assertEqual(employee_data['name'],
                         "Raj", "Employee Name not matching.")
        self.assertEqual(employee_data['age'],
                         30, "Employee Age not matching.")
        self.assertEqual(employee_data['dept'],
                         "IT", "Employee Age not matching.")
        self.assertIsNotNone(
            employee_data['project'], "Employee doesnt have project object ")
        self.assertEqual(
            employee_data['project'][0]['name'], "Login Module", "Employee project.name doesnt match ")
        self.assertEqual(
            employee_data['project'][0]['tenure'], 3, "Employee project.tenure doesnt match ")


if __name__ == '__main__':
    unittest.main()