# importing modules
import time
import pyautogui
 
# returns a size object with
# width and height of the screen
print(pyautogui.size())
print(pyautogui.position())

l, t, w, h = pyautogui.locateOnScreen('logo.png')
pyautogui.moveTo(l+(w/2),t+(h/2), duration = 1)

l, t, w, h = pyautogui.locateOnScreen('dots.png')  
pyautogui.moveTo(l+(w/2),t+(h/2), duration = 1)
 
try: 
    while True:

        try:
            l, t, w, h = pyautogui.locateOnScreen('deviceontrue.png')
            print(l, t, w, h)
            pyautogui.moveTo(239,426, duration = 1)
            pyautogui.doubleClick()
            pyautogui.typewrite("false")
        except:
            print('<True> Text Not found')

        try:
            l, t, w, h = pyautogui.locateOnScreen('deviceonfalse.png')
            print(l, t, w, h)
            pyautogui.moveTo(239,426, duration = 1)
            pyautogui.doubleClick()
            pyautogui.typewrite("true")
        except:
            print('<False> Text Not found')

        try:    
            l, t, w, h = pyautogui.locateOnScreen('update.png')
            print("Update Button", l, t, w, h)
            pyautogui.moveTo(l+(w/2),t+(h/2), duration = 1)
            pyautogui.click()
        except:
            print('Update Button Not found')

        time.sleep(5)
        
        try:
            l, t, w, h = pyautogui.locateOnScreen('greentab.png')
            print("Green Tab", l, t, w, h)
            pyautogui.moveTo(1330,178, duration = 1)
            pyautogui.click()
        except:
            print('Green Tab Not found')   

        time.sleep(2)        

        try:
            l, t, w, h = pyautogui.locateOnScreen('refresh.png')
            print("Refresh Button", l, t, w, h)
            pyautogui.moveTo(l+(w/2),t+(h/2), duration = 1)
            pyautogui.click()
        except:
            print('Refresh Button Not found')
        
        time.sleep(5)
        
        try:
            l, t, w, h = pyautogui.locateOnScreen('edit.png')
            print("Edit Button", l, t, w, h)
            pyautogui.moveTo(l+(w/2),t+(h/2), duration = 1)
            pyautogui.click()
        except:
            print('Edit Button Not found')
                    
        print("Try again")
        time.sleep(15)

except KeyboardInterrupt:
    print('\nDone.')
