import unittest

from eleven_three import Employee

class TestEmployee(unittest.TestCase):
    """Test that the methods of Employee work properly."""

    def setUp(self):
        self.employee = Employee('Cate', 'Fritz', 100000)

    def test_give_raise_no_arguments(self):
        self.employee.give_raise()
        self.assertEqual(105000, self.employee.salary)

    def test_give_raise_arguments(self):
        self.employee.give_raise(10000)
        self.assertEqual(110000, self.employee.salary)

unittest.main()