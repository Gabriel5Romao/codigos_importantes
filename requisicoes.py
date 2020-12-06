"""
Trabalhando com requests e beautifulsoup4

1. pip install requests e beautifulsoup4

requests:
    Responsável por entrar na rede. Pode obter JSON de APIs.

beautifulsoup:
    Responsável por trabalhar com os dados, como por exemplo obter o html da página.
"""

import requests
from bs4 import BeautifulSoup as bs

if __name__ != "__main__":


    # Função get, que faz uma requisição do tipo get tem como parâmetro a url eauth=("usuário","senha") é opcional. 
    # Para se alterar o tipo de requisição(POST, DELETE,...) basta trocar o get pela palavra em minúsuclo. 
    # Um parâmetro opcional e importante é timeout=x, que interromperá a conexão após x segundos

    requisicao = requests.get("url",auth=("user","pass"))

    requisicao.status_code
    # Informando parâmetros
    parametros = {"par1": "valor1", "par2" : "valor2"}
    requisicao = requests.get("url",params=parametros)

    # Retorna o código fonte da página
    requisicao.text

    # Retorna a codificação da página (UTF-8 por exemplo)
    requisicao.encoding

    # Retorna um JSON, útil quando você trabalhar com JSON
    requisicao.json

    # Retorna o status da requisição
    requisicao.status_code

    # - BeautifulSoup - #

    # Armmazena um documento html
    sopa = BeautifulSoup(html,'html.parser')
    
    # Converte para um html bonito de se ver
    sopa.prettify()

    # Retorna o title da página 
    sopa.title.string

    # Retorna a primeira tag desejada
    sopa.tag_html

    # Retorna a classe da primeira tag pesquisada
    sopa.tag_html['class']

    # Retorna uma lista com todas as tags procuradas
    sopa.find_all('tag_html')

    # Retorna um atributo ou tag desejada. De preferência consulte a doc
    sopa.find(id="id_de_elemento")

    # Extração de um atributo; a partir de uma tag html, por exemplo a, você pode capturar algum atributo, por exemplo um link, class...
    bs4_element.get('href')
    
else:

    requisicao = requests.get("http://pudim.com.br/")
    codigo_fonte = requisicao.text # Aqui temos o html da página

    soup = bs(codigo_fonte,'html.parser')
    tag = soup.find(name='img')

    print(tag.get('src'))

