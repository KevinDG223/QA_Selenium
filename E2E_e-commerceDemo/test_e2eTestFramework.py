import json

import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage
test_data_path = 'D:\\Kevin\\Escritorio\\Py\\Selenium_webdriver\\Dia_5\\Seccion_19\\data\\test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopPage = loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    shopPage.add_product_to_cart(test_list_item["productName"])
    print(loginPage.getTitle())
    checkout_confirmation = shopPage.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("India")
    checkout_confirmation.validate_order()


