# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar o driver do navegador (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

# Abrir o Mercado Livre
driver.get("https://www.mercadolivre.com.br/")

# Encontrar a barra de pesquisa e buscar um produto
busca = driver.find_element(By.NAME, "as_word")
busca.send_keys("notebook gamer")  # Substitua pelo produto que deseja buscar
busca.send_keys(Keys.RETURN)

# Esperar os resultados carregarem
time.sleep(3)

# Esperar o campo de preço aparecer
try:
    # Aguardar até o campo de preço mínimo ser visível
    campo_preco_min = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="De"]'))
    )
    
    # Aguardar até o campo de preço máximo ser visível
    campo_preco_max = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Até"]'))
    )
    
    # Definir os valores de preço mínimo e máximo
    preco_min = 2000
    preco_max = 5000

    # Preencher os campos com os valores de faixa de preço
    campo_preco_min.clear()
    campo_preco_min.send_keys(str(preco_min))

    campo_preco_max.clear()
    campo_preco_max.send_keys(str(preco_max))

    # Aplicar o filtro pressionando Enter no campo de preço máximo
    campo_preco_max.send_keys(Keys.RETURN)

except Exception as e:
    print(f"Erro ao aplicar filtro de preço: {e}")
    driver.quit()
    exit()

# Esperar os resultados carregarem após a aplicação do filtro
time.sleep(5)

# Capturar os preços dos produtos filtrados
precos = driver.find_elements(By.CLASS_NAME, "andes-money-amount__fraction")  # Classe onde estão os preços

# Exibir os preços no terminal
for i, preco in enumerate(precos[:5]):  # Exibir os 5 primeiros preços
    print(f"Produto {i+1}: R$ {preco.text}")

# Fechar o navegador
driver.quit()
