import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from time import sleep

item = input('Qual item minerar? ')
dados_consulta = []

options = Options()
options.add_argument('window-size=1080,720')
navegador = webdriver.Edge(options=options)

navegador.get('https://best.aliexpress.com/')

sleep(0.5)

input_place = navegador.find_element(By.CLASS_NAME, 'search-key')
input_place.send_keys(item)
sleep(0.5)
input_place.submit()

sleep(0.5)

try:
    navegador.execute_script('window.scrollBy(0, 1000)')
except:
    None

sleep(0.5)

conteudo_pagina = navegador.page_source

site = BeautifulSoup(conteudo_pagina, 'html.parser')

produtos = site.findAll('a', attrs={'class': 'manhattan--container--1lP57Ag cards--gallery--2o6yJVt'})

for produto in produtos:

    nome = produto.find('h1', attrs={'class': 'manhattan--titleText--WccSjUS'})
    nome = nome.text

    url = 'https:'+produto['href']

    preco = produto.find('div', attrs={'class': 'manhattan--price-sale--1CCSZfK'})
    preco = preco.text

    print("Nome", nome)
    print(preco)
    print("URL: "+url)

    dados_consulta.append([nome, preco, url])

    print()

dados = pd.DataFrame(dados_consulta, columns=['Nome', 'Preço', 'Link'])
dados.to_csv(item+'.csv', index=False)
