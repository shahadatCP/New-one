import pyautogui
from time import sleep
n = int(input())
sleep(3)
pyautogui.write(str(n))
pyautogui.press('enter')
for i in range (0, n):
    for j in range(0, i+1):
        pyautogui.write('#', interval = 0.05)
    pyautogui.press('enter')



