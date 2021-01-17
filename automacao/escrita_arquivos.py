"""
Para escrever arquivos no python, usamos a função open que retorna um arquivo.

É possível combinar a função open() com o pacote requests para fazer o download, bastando só acessar o site
e baixar o arquivo no formato de bytes.

SINTAXE:

    with open(str:'nome_do_arquivo.extensao',str:'modo_de_abertura') as nome_para_trabalhar:
        Aqui usamos métodos do objeto nome_para_trabalhar com o intuito de ler/gravar arquivos

ACRESCENTE encoding='utf-8' AO MÉTODO OPEN CASO TENHA PROBLEMAS NA FORMATAÇÃO.
"""
# Principais modos

with open('teste.txt', 'w') as teste:
   teste.write("O modo w na escrita de arquivos, cria e abre para escrita. Deletando o arquivo se já tiver algo escrito")

with open('teste.txt', 'a') as teste:
   teste.write("\nO modo a, soma algum texto no final do arquivo")

with open('teste.txt','r') as arquivo:
   conteudo = arquivo.read()
   lista_de_linhas = arquivo.readlines()

print(conteudo)
print(lista_de_linhas)

# Bixando arquivos que não são texto

import requests as r

link_download = r.get("http://builds.openlogicproject.org/courses/phil310/phil310-letter.pdf")

with open("livro_logica.pdf", "wb") as livro:
   #Aqui o modo passado foi wb para escrita em modo binário.

   livro.write(link_download.content)
   #Devemos escrever no arquivo o conteúdo da requisição.