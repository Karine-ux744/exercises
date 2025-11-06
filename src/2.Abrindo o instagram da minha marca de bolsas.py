
#o comando pyautogui.PAUSE faz o programa esperar os segundos que eu estipulei entre cada ação

# OBJETIVO: abrir o Instagram @lyne.bolsas
# apertar o windows
# digitar chrome
# apertar enter
# clicar na guia que vai abrir
# selecionar o primeiro usuário que aparecer
# apertar enter
# digitar a url do instagram
# apertar enter

import pyautogui
import time 

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=848, y=524)
pyautogui.click(x=449, y=381)
pyautogui.hotkey("ctrl","t")
pyautogui.write("instagram.com/lyne.bolsas")
pyautogui.press("enter")

