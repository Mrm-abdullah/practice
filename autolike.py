import pyautogui
import time
pyautogui.FAILSAFE = False
for i in range(1,5):
    time.sleep(5)
    pyautogui.press("j")
    time.sleep(3)
    pyautogui.press('l')
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')
    
