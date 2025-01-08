import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=cotacao+dolar"

requisicao = requests.get(url)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, 'html.parser')

titulo = site.find('title')
print(titulo)

