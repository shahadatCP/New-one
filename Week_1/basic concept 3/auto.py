import pyautogui
from time import sleep
n = int(input())
sleep(5)
for i in range(0, n):
    pyautogui.write('Honestly I\'m not typing', interval = 0.00001)
    pyautogui.press('enter')
    pyautogui.displayMousePosition


