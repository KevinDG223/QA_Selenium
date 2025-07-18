from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"D:\Kevin\Documents\Webdriver\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)
driver.implicitly_wait(2)
#Máximo 5 segundo de espera, si se tienen 2 segundos se guardan 3.
#Es global, por lo que se aplicará en casos especificos.

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

#Separacion de nombres
frutas = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-last-child(4) p")
lista_frutas = [fruta.text.split(" - ")[0] for fruta in frutas]
print(lista_frutas)

#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "TR TD:NTH-CHILD(5) P")
sum = 0

for price in prices:
    sum = sum + int(price.text)        #48 + 160 + 180

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totamt").text)

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
totalDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(totalDiscount)
assert totalDiscount < totalAmount


time.sleep(5)