import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge", help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(4)
    elif browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
    yield driver
    driver.close()

