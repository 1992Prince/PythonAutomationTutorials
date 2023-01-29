import pytest

"""
We are defining scope of below fixture with decorator inside parentesis
below fixture will be executed once before all tcs and after all tcs
here we can give any name to function name
"""
@pytest.fixture(scope='module')
def setup_module():
    print("Creating DB Connection")

    yield
    print("Closing DB connection")

"""
We are defining scope of below fixture with decorator inside parentesis
below fixture will be executed before each tc and after each tc
here we can give any name to function name
"""
@pytest.fixture(scope='function')
def setup_function():
    print("Launching the browser")

    yield
    print("Quitting the browser")

"""

# setup_module will be kept first and setup_function should be kept in second pos

def test_dologin(setup_module,setup_function):
    print("Executing login testcase")

def test_user_reg(setup_module,setup_function):
    print("Executing registration testcase")
    
# also above function can be defined like below also
    
"""
@pytest.mark.usefixtures("setup_module","setup_function")
def test_dologin():
    print("Executing login testcase")

@pytest.mark.usefixtures("setup_module","setup_function")
def test_user_reg(setup_module,setup_function):
    print("Executing registration testcase")
