"""
pip install pyautogui

Serve para navegar com mouse, clicando e arrastando.
           enviar dados do teclado como atalhos e outras teclas.
"""

import pyautogui as pa

# Métodos para trabalhar com dados do MONITOR
pa.size()  # retorna uma tupla com a largura x altura do monitor primário
largura, altura = pa.size()  # boa prática guardar a largura e altura em variáveis

# Métodos para o MOUSE
x, y = pa.position()  # retorna uma tupla contendo a posição X e a posição Y do mouse
pa.moveTo(largura / 2, altura / 2, duration=3)  # Move o mouse para a posição indicada. O parâmetro duration é opcional
pa.move(0, 10)  # Essa função é um movimento relativo, tomando como base a atual posição do mouse.
pa.click()  # Clica
pa.click(largura / 2, altura - 300, clicks=2, interval=1, button="PRIMARY",
         duration=3)  # Move o cursor para a posição, executando certos clicks, com um certo intervalo, com o botão
# PRIMARY(str) e uma duração para mover o mouse. Nenhum desses parâmetros são obrigatórios.
pa.scroll(3)  # Executa o scroll pra baixo do mouse 3 vezes
# pa.click('django.pdf') # Procura na tela onde aparece o texto fornecido e clica nele


# Métodos de TECLADO
pa.write("texto", interval=0.1)  # Escreve um texto fornecido com intervalo de 0.1s em cada caractere
pa.press("enter")  # aperta um botão informado. Pode passar uma lista com botões. Pode acresccentar o parâmetro
# presses=int
print(pa.KEY_NAMES)  # Retorna a lista dos botões que podem ser utilizados com a função press
pa.hotkey("ctrl", "c")  # Pressiona mais de um botão. Muito útil para acionar atalhos.
pa.keyDown("shift")  # Aperta e mantém pra baixo a teclado informada. Deve ser usada com keyUp para soltar a tecla
pa.keyUp("shift")

# Outros métodos
pa.alert(text='teste', title='titulo',
      button='OK')  # Faz aparecer uma janela com os parâmetros dados. O programa pausa e volta quando o usuário
# apertar ok

pa.confirm(text='Confirm', title='Janela Confirm', buttons=['OK', 'Cancel'])  # Aparece uma janela de confirmação pro usuário.
print(pa.prompt(text='Prompt', title='Janela Prompt', default='')) # prompt que retorna o que o usuário digitou, pode ser usado sem print
pa.password(text='Senha', title='Janela de Senha', default='', mask='*') # prompt para senha