import pytest

def test_validateTile():
    expectedtitle = "Google.com"
    actualtitle = "Gmail.com"
    title = "This is Gmail Website"

    assert expectedtitle == actualtitle ,"Title are not matching"
    # this will validate "Gmail" text in title
    assert "Gmaila" in title,"Text is not present in title"
    assert False, "Forcefully failing test"

"""
If u want to run above tests as soft assertion then run below command :
pytest test_5thAssertions.py --soft-asserts   
dont pass -s or -v with above command 
pip install pytest-soft-assertions : command to install soft assertion in pytest
"""
