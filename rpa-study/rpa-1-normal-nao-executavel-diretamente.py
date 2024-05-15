# Retirei o atributo chmod +x (executável) do arquivo e mantive o padrão: bash #!/usr/bin/bash #!/usr/bin/env python3 mas pode ser que tornar executável seja interessante para rodar este script Python no Windows... não sei... só testando mesmo...
import pyautogui
import time
time.sleep(3)
pyautogui.moveTo(100, 100, duration=0.25)

pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(0, 0, duration=0.25)
# pyautogui.moveTo(1365, 767, duration=0.25)




# Após mover o mouse até as coordenadas X e Y, e dar 1 clique, o teclado escreverá “Hello World!” no local designado
pyautogui. typewrite('Hello World! ')

# Clique no botão "Arquivo" no menu
pyautogui.click(x=100, y=100)

# Espere um segundo
time.sleep(1)

# Clique em "Abrir" no menu suspenso
pyautogui.click(x=100, y=150)

# Espere um segundo
time.sleep(1)

# Digite o nome do arquivo a ser aberto
pyautogui.write("exemplo.txt")

# Pressione Enter para confirmar
pyautogui.press("enter")

