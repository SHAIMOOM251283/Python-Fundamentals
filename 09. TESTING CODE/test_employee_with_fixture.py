import pytest
from employee import Employee

@pytest.fixture
def emp_instance():
    # Create an instance of Employee
    emp = Employee("John", "Doe", 50000)
    return emp

def test_give_default_raise(emp_instance):
    # Call the give_raise method without specifying raise_amount
    emp_instance.give_raise()
        
    # Check if the annual_salary increased by the default amount (5000)
    assert emp_instance.annual_salary == 55000

def test_give_custom_raise(emp_instance):
    # Call the give_raise method with a custom raise_amount
    emp_instance.give_raise(7000)
        
    # Check if the annual_salary increased by the custom amount (7000)
    assert emp_instance.annual_salary == 57000  # Assuming a typo in the expected value, as per the previous test.
