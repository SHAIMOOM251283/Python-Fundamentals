import pytest
from employee import Employee

def test_give_default_raise():
    # Create an instance of Employee
    emp = Employee("John", "Doe", 50000)
        
    # Call the give_raise method without specifying raise_amount
    emp.give_raise()
        
    # Check if the annual_salary increased by the default amount (5000)
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    # Create an instance of Employee
    emp = Employee("Jane", "Smith", 60000)
        
    # Call the give_raise method with a custom raise_amount
    emp.give_raise(7000)
        
    # Check if the annual_salary increased by the custom amount (7000)
    assert emp.annual_salary == 67000
