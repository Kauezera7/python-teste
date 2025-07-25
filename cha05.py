from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


navegador = webdriver.Chrome()


navegador.get("https:")


time.sleep(2)


navegador.find_element(By.ID, "username").send_keys("tomsmith")


navegador.find_element(By.ID, "password").send_keys("SuperSecretPassword!")


navegador.find_element(By.ID, "password").send_keys(Keys.RETURN)


time.sleep(5)


navegador.quit()
