import pytest


@pytest.mark.usefixtures("setup")
class Test_ClassLevelFix:

    def test_FourthTC(self):
        print("I am fourth tc")

    def test_FifthTC(self):
        print("I am fifth tc")
