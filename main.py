import pyautogui
import cv2 as cv
import numpy as np
from time import time
import random
import os
from windowCapture import WindowCapture


wincap = WindowCapture('RuneLite')

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)
    # cv.resizeWindow('Computer Vision', 940, 730)

    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

def setCamera():
    camera = pyautogui.locateCenterOnScreen('images/compass.png', confidence=0.8)
    pyautogui.moveTo(camera, duration=0.5)
    pyautogui.click()


# # GAME SIZE = 900 x 700
# run = True
# while run:
#     setCamera()
#     equip()
#     run = False
    