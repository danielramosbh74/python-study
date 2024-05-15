import pyautogui
import time

# Aguarde alguns segundos antes de começar 
# (tempo para abrir o aplicativo alvo)
time.sleep(5)

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
