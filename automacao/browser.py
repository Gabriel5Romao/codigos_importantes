"""
pip install selenium

O selenium webdriver corresponde ao biblioteca para controle do navegador;
           IDE corresponde as extensões nos navegadores para gravar ações do usu
           ário;    
           Grid serve para rodar testes fora da máquina de desenvolvimento; 

Drivers necessários para cada navegador. É necessário que eles estejam como vari
áveis de ambiente.
https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
    
"""
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
driver = Firefox()  # Ou outro navegador, também podemos fazer with Firefox() 
#as driver


# Navegação do Browser
driver.get("https://github.com")  # Insere o site que você deseja ir
driver.current_url
driver.back()  # Faz a opção de voltar para página anterior
driver.forward()  # Avança no histórico
driver.refresh()  
driver.title  # Retorna o Title do html da página
driver.close()  # Fecha a janela ou aba
driver.quit()  # Fecha o browser e finaliza a sessão


# Localizando elementos no Browser
driver.find_element_by_name("q")  # Existem várias formas de encontrar elementos como id, tag name... busque por elements para ter uma lista
# Armazene esse elemento em uma variável e você pode iterar o processo para encontrar um elemento nessa variável
# Um web element tem o atributo text para obter o texto dele.


# Gerenciamento de Tela
driver.get_window_size()  # Retorna uma tupla largura x altura. Pode acrescentar o método get("width") ou height pra especificar um dos dois
driver.set_window_size(1000,1000)
driver.get_window_position()  # Retorna tupla com a coordenada do canto superior esquerdo
driver.set_window_position(0,0)
driver.maximize_window()
driver.minimize_window()


# Trabalhando com condições e espera
wait = wdw(driver,1)  # O primeiro argumento é a instância do driver, o segunto é um tiemout
wait.until(ec.number_of_windows_to_be(2))  # Esse parâmetro faz uma espera até que a condição de janelas seja dois
wait.until(ec.title_is)  # Existem muitos parâmetros interessantes nesse expected conditions, sempre bom fazer o dir


# Navegando entre abas
# É preferível usar pyautogui, mais fácil e mais legível. https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/



