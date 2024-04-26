import pyautogui
import cv2 as cv
import numpy as np
from time import time
import random
import os
import win32gui, win32ui, win32con


window_name = 'RuneLite'

def window_capture():
    # DEFINE WIDTH AND HEIGHT
    w = 940
    h = 730

    # GET WINDOW IMAGE DATA
    hwnd = win32gui.FindWindow(None, window_name)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    # SAVE SCREENSHOT
    # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # FREE UP RESOURCES
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img

loop_time = time()
while(True):

    screenshot = window_capture()

    cv.imshow('Computer Vision', screenshot)
    cv.resizeWindow('Computer Vision', 940, 730)

    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

def setCamera():
    camera = pyautogui.locateCenterOnScreen('images/compass.png', confidence=0.8)
    pyautogui.moveTo(camera, duration=0.5)
    pyautogui.click()


window_capture()

# # GAME SIZE = 900 x 700
# run = True
# while run:
#     setCamera()
#     equip()
#     run = False
    