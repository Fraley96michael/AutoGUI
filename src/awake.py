import pyautogui
import time
import sys
from datetime import datetime

while True:
    try:
        pyautogui.moveTo(905, 540, duration=0.25)
        pyautogui.moveTo(920, 540, duration=0.25)
      

      


    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit()
