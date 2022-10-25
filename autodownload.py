import pyautogui
import time
pyautogui.FAILSAFE = False
for i in range(48, 67):
    time.sleep(3)
    pyautogui.moveTo(142, 51, 2)
    time.sleep(1)
    pyautogui.click(142, 51, 1)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(142, 51, 1)
    time.sleep(1)
    pyautogui.press('s')
    time.sleep(1)
    pyautogui.press('s')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.moveTo(665, 582, 2)
    time.sleep(1)
    pyautogui.click(665, 582, 1)
    time.sleep(10)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.hotkey('shift', 'n')
    time.sleep(1)



    # pyautogui.press('ctrl + t')
    #time.sleep(1)
#    time.sleep(1)
 #   pyautogui.press('enter')
  #  time.sleep(5)
   # for i in range(1, 17):
    #    print(i)
     #   pyautogui.press('tab')
      #  time.sleep(0.3)
    #pyautogui.press('enter')
    

    
    