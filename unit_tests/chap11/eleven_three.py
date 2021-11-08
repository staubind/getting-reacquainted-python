
class Employee():
    """Model an employee's information."""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, pay_raise=5000):
        self.salary += pay_raise

    