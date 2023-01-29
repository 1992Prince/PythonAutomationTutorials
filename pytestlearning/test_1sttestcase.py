import pytest

# below fun will be executed before all tcs only once
def setup_module(module):
    print("Creating db connection")

# below fun will be executed after all tcs only once
def teardown_module(module):
    print("Closing db connection")

# below function will be executed before each testcase
def setup_function(function):
    print("launching the browser")

# below function will be executed after each testcase
def teardown_function(function):
    print("Quitting the browser")

def test_dologin():
    print("Executing login testcase")

def test_user_reg():
    print("Executing registration testcase")
