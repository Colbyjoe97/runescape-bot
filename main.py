import pyautogui
import cv2 as cv
import numpy as np
from time import time
import random
import os
from windowCapture import WindowCapture
from vision import findClickPositions



# Click in a random spot between given px values
def randNum(min, max):
    randNum = random.randint(min, max)
    return randNum

# Set camera to North 
def setCamera():
    camera = pyautogui.locateCenterOnScreen('images/misc/compass.png', confidence=0.8)
    pyautogui.moveTo((camera[0]+randNum(-10, 10)), (camera[1]+randNum(-10, 10)), duration=0.5)
    pyautogui.click()

# GAME SIZE = 900 x 700
setCamera()
# run = True
# while run:
#     setCamera()
#     run = False
    