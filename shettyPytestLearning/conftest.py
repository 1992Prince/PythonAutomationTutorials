import pytest


"""
in below setup we can write browser invocation and closing code
"""
@pytest.fixture()
def setup():
    print("I will be executing first")

    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul","Shetty","rs@mail.com"]

@pytest.fixture(params=["chrome","Firefox","InternetExplorer","Edge"])
def parametrizationdataLoad(request):
    return request.param

@pytest.fixture(params=[("chrome","Firefox","chrofox@gmail.com"),("Interlorer","Edge","IEdge@mail.com")])
def parametrizationdataLoad2(request):
    return request.param

@pytest.fixture(params=[{"fname":"Prince","age":30,"company":"Accenture"},{"fname":"Rishab","age":27,"company":"IAS"}])
def parametrizationdataLoad3(request):
    return request.param

