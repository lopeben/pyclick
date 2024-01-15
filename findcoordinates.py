# importing modules
import time
import pyautogui
 
# returns a size object with
# width and height of the screen

try:
    while True:
        print(pyautogui.position())
        time.sleep(1)
except KeyboardInterrupt:
    print('\nDone.')