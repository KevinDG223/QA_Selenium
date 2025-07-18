from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
    service_obj = Service(r"D:\Kevin\Documents\Webdriver\msedgedriver.exe")
    driver = webdriver.Edge(service=service_obj)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # Click on column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # collect all  veggie names -> veggieList
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for ele in veggieWebElements:
        browserSortedVeggies.append(ele.text)

    originalBrowserSortedList = browserSortedVeggies.copy()
    # Sort this veggieList => newSortedListed
    browserSortedVeggies.sort()

    assert browserSortedVeggies == originalBrowserSortedList

    time.sleep(2)

