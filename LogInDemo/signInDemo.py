from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(r"D:\Kevin\Documents\Webdriver\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hellorahul@gmail.com")     # Al inspeccionar se cuenta con la clase NAME
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")      # este solo tiene ID por lo que se utiliza = exampleInputPassword1
driver.find_element(By.ID, "exampleCheck1").click()                         # Mismo caso que arriba

# Xpath - //tagname[@attribute = 'value'] -> //input[@type = 'submit']
# CSS - //tagname[attribute = 'value'] -> //input[type = 'submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text

print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()




time.sleep(30)