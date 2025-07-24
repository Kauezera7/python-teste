from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Cria uma instância do navegador (Chrome)
navegador = webdriver.Chrome()

# Acessa a página de login
navegador.get("https://the-internet.herokuapp.com/login")

# Aguarda 2 segundos para garantir que a página carregou
time.sleep(2)

# Localiza o campo de usuário e digita
navegador.find_element(By.ID, "username").send_keys("tomsmith")

# Localiza o campo de senha e digita
navegador.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Submete o formulário pressionando ENTER
navegador.find_element(By.ID, "password").send_keys(Keys.RETURN)

# Aguarda para visualização do resultado
time.sleep(5)

# Encerra o navegador
navegador.quit()
