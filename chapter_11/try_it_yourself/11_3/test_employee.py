import pytest
from employee import Employee

@pytest.fixture
def employee():
    "The default employee data"
    employee = Employee("elon", "musk", 30_000)
    return employee

def test_give_default_raise(employee):
    """testing default raise """
    employee.give_raise()
    assert employee.first_name == "elon"
    assert employee.last_name == "musk"
    assert employee.annual_salary == 35_000

def test_give_custom_raise(employee):
    """testing a 10k raise """
    employee.give_raise(10_000)
    assert employee.first_name == "elon"
    assert employee.last_name == "musk"
    assert employee.annual_salary == 40_000