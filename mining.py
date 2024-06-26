import pyautogui
import random
import os
import cv2 as cv
import numpy as np
from time import time
from main import setCamera, randNum
from windowCapture import WindowCapture
from vision import Vision

# initialize WindowCapture class
wincap = WindowCapture('RuneLite')

# initialize Vision class
vision_copper = Vision('images/resources/ore/copper.jpg')

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()

    # display processed image
    points = vision_copper.find(screenshot, 0.6, 'rectangles')

    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    # SET POINT TO THE NEWEST ORE FOUND AND CLICK
    # point = points[0]
    # pyautogui.moveTo(points[0][0]-randNum(-20, 0), points[0][1]-randNum(-20, 0), duration=1)
    # pyautogui.click()
    # pyautogui.sleep(randNum(15, 20))
