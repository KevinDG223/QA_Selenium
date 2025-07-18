# Any pytest file should start with the test_
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest

@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
