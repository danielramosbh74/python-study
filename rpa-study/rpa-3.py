#!/usr/bin/env python3
# O padrão é o bash #!/usr/bin/bash #!/usr/bin/env python3

# Para saber a posição do mouse:
# xdotool getmouselocation

import pyautogui
# import pyautogui as pg
import time

# time.sleep(5)
# pyautogui.moveTo(15, 37, duration=0.25)
# OU
# pg.moveTo(15, 37, duration=0.25)
# Posição do menu "File" no VS Code do Linux Mint usando o X.org, descoberta usando o comando xdotool getmouselocation

# x = 0
# y = 0
# try:
#     while True:
#         time.sleep(5)
#         x, y = pyautogui.position()
#         print (x, y)
#         a = pyautogui.pixel(x, y)
#         print (a)
#     input("Press Enter to continue...")
# except KeyboardInterrupt:
#     quit()


time.sleep(5)
# pyautogui.moveTo(503, 362, duration=0.25)
pyautogui.dragTo(160, 290, duration=0.25)
pyautogui.hotkey('ctrl', 'c')

time.sleep(5)
pyautogui.hotkey('ctrl', 'v')


# Após mover o mouse até as coordenadas X e Y, e dar 1 clique, o teclado escreverá “Hello World!” no local designado
# pyautogui. typewrite('Hello World! ')

# Clique no botão "Arquivo" no menu
# pyautogui.click(x=100, y=100)


# Clique em "Abrir" no menu suspenso
# pyautogui.click(x=100, y=150)

# Espere um segundo
# time.sleep(1)

# Digite o nome do arquivo a ser aberto
# pyautogui.write("exemplo.txt")

# Pressione Enter para confirmar
# pyautogui.press("enter")
