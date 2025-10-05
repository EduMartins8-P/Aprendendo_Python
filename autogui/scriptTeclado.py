import pyautogui
import time

pyautogui.click(4200, 1373)
time.sleep(0.5)
pyautogui.write("Ola", interval=0.05)
pyautogui.write(" fulano ", interval=0.05)
pyautogui.press('enter')