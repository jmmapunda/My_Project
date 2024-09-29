import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
lang = driver.find_element(By.ID, "langSelect-EN")
lang.click()
time.sleep(5)


# this loop will click the cookie 20 times and always pick first upgrade and will buy the highest product first
while True:
    for n in range(20, -1, -1):
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
        try:
            upgrade = driver.find_element(By.ID, f"upgrade0")
            upgrade.click()
        except:
            pass
        try:
            product = driver.find_element(By.ID, f"product{n}")
            product.click()
        except:
            pass






time.sleep(10)
