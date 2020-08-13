import pyautogui
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")





import pyautogui, time
time.sleep(6)
screenshot = pyautogui.screenshot()
screenshot.save("screenshot1.png")





from PIL import ImageGrab
image = ImageGrab.grab(bbox=(0,0,700,800))
image.save('sc.png')





# pip install keyboard
from PIL import ImageGrab
import keyboard
while True:
    try:
        if keyboard.is_pressed('p'):
           image = ImageGrab.grab()
           image.save("screenshot.png")
           break
        else:
            pass
    except:
        break





import pyautogui   # import PyAutoGUI library
import tkinter as tk  # import tkinter library
# create main window
window = tk.Tk()
# define a method that will call whenever button will be clicked
def take():
    image = pyautogui.screenshot("tkscreen.png")
# create a button 
shot_btn = tk.Button(window,text = "Take Screenshot", command= callback)
# place the button on the window
shot_btn.place(x=50, y=50)
window.mainloop()