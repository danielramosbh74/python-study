# Para saber a posição do mouse:
# xdotool getmouselocation

import pyautogui
import time
time.sleep(3)
pyautogui.moveTo(15, 37, duration=0.25)
# Posição do menu "File" no VS Code do Linux Mint usando o X.org, descoberta usando o comando xdotool getmouselocation
