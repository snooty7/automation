import threading
import pyautogui

def printit():
  threading.Timer(5.0, printit).start()
  pyautogui.scroll(-45)
  pyautogui.scroll(45)

printit()