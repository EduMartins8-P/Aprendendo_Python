import pyautogui
import time

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

coords = [
    (576, 948),
    (1091, 941),
    (1595, 926)
]

pyautogui.hotkey("ctrl", "esc")
time.sleep(0.5)
pyautogui.write("firefox")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("rewards.bing.com")
pyautogui.press('enter')
time.sleep(5)
for x, y in coords:
    pyautogui.click(x, y)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.5)

for letra in letras:
    pyautogui.click(886, 659)
    pyautogui.press("backspace")
    pyautogui.write(letra)
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.3)

pyautogui.scroll(-2000)
pyautogui.scroll(-500)
time.sleep(0.3)
for x, y in coords:
    pyautogui.click(x, y)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.5)

pyautogui.hotkey("ctrl", "esc")
time.sleep(0.5)
pyautogui.write("xbox")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(1063, 53)
time.sleep(0.5)
pyautogui.write("minesweepe")
pyautogui.write("r")
time.sleep(1.5)
pyautogui.click(1040, 157)
time.sleep(1)
pyautogui.click(464, 512)
time.sleep(40)
pyautogui.click(242, 385)
time.sleep(2)
for i in range(180):
    pyautogui.click(552, 412, button='right')
    time.sleep(3)
    pyautogui.click(886, 397, button='right')
    time.sleep(3)