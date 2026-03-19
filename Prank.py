
import pyautogui as rudraa
import time

message = "Hello, this is automated message!"
time.sleep(5)  # give you time to click on the chat/input box

for i in range(10):
    rudraa.write(message)
    rudraa.press("enter")
    time.sleep(0.5)