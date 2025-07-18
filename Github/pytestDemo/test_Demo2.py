# Any pytest file should start with the test_
# pytest method names should start with test
# Any code should be wrapped in method only
# method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# You can run specific file with py.test <filename>
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# You can skip tests with @pytest.mark.skip
# Fixtures are used as setup and tear down methods fore test cases- conftest file to generalize fixture and make it available to all test cases
# data driven and parameterization can be done with retunr statements in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest



def test_firstProgram():
    msg = "Hello" #operations
    assert msg == "Hi", "Test failed because strings do not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"

