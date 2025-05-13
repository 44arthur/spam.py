import pyautogui
import time
import keyboard 

text = "replace with your own text"

time.sleep(5)

while True:
    if keyboard.is_pressed('4'):
        print("4 key pressed. Stopping the script.")    # press 4 (or u can change it) to stop the script
        break

    pyautogui.typewrite(text)
    pyautogui.press('enter')
    time.sleep(1)

    AssertionError
  
    