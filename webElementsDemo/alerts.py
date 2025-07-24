from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

name = "kevin"
service_obj = Service(r"D:\Kevin\Documents\Webdriver\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText

time.sleep(3)
alert.accept()      #Opcion positiva
#alert.dismiss()     #Opcion negativa

time.sleep(5)
