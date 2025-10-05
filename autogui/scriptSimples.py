import pyautogui
import time
from pynput import keyboard

stop_script = False

def on_press(key):
    global stop_script
    if key == keyboard.Key.space:  
        stop_script = True

listener = keyboard.Listener(on_press=on_press)
listener.start()

start_time = time.time()

while True:
    if stop_script:
        print("Automação parada pelo usuário!")
        break

    pyautogui.click(12, 121)
    time.sleep(0.5)
    pyautogui.click(131, 1074)
    time.sleep(0.5)
    pyautogui.click(12, 121)
    time.sleep(3.0)
    pyautogui.click(1061, 702)
    time.sleep(0.8)
    pyautogui.click(1061, 702)
    time.sleep(0.5)
