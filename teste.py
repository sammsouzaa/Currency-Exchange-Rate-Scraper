from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")

# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

moedas = {"Dolar", "Euro", "Peso argentino", "Kwanza", "Won"}

for moeda in moedas:
    driver.get(f"https://google.com/search?q={moeda}+hoje")
    valor = driver.find_element(By.CLASS_NAME,"SwHCTb")
    print(f"1 {moeda} equivale a {valor.text} reais brasileiros")

driver.quit()