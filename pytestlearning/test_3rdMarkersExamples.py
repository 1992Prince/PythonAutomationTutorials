import pytest

"""
From command prompt if u want to run any single tc from this file then 
use command : pytest test_3rdMarkersExamples.py -s -v -k dologin
              :or
              pytest test_3rdMarkersExamples.py -s -v -k user_reg
              
Like testng, we can assign group also to each tcs i.e. here we call it marker

From command prompt if u want to run any single group from this file then 
use command : pytest test_3rdMarkersExamples.py -s -v -m functional
"""

# for below tc we have assigned it functional tc
@pytest.mark.functional
def test_dologin():
    print("Executing login testcase")

# for below tc we have assigned it regression tc
@pytest.mark.regression
def test_user_reg():
    print("Executing registration testcase")

# for below tc we have assigned it functional tc
@pytest.mark.functional
def test_compose_Email():
    print("Executing compose email testcase")
