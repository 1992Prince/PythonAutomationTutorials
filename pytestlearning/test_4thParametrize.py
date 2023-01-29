import pytest

def get_data():
    return [
        ("pkp@mail.com","pkp123"),
        ("rkp@mail.com","mkp123"),
        ("skp@mail.com","skp123")
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_doLogin(username,password):
    print(username, "----", password)
