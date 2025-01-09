import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=cotacao+dolar"
headers = {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

requisicao = requests.get(url, headers=headers)
print(requisicao)

site = BeautifulSoup(requisicao.text, 'html.parser')

cotacao = site.find('span', class_='hgKElc')
print(cotacao)


