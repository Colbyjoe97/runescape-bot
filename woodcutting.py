import pyautogui
from main import setCamera
import random
import os
import cv2
import numpy as np

window_name = 'RuneLite'

# UNIVERSAL FUNCTIONS
def moveRandom(img):
    x = random.random()*-img.width
    y = random.random()*-img.height
    pyautogui.moveTo((img.left-x), (img.top-y), duration=0.5)


# FINDING BANKER
bankerList = 'images/banker'
img_list = os.listdir(bankerList)
print(img_list)

def bank():
    for img in img_list:
        try:
            current_img = pyautogui.locateOnScreen(f'images/banker/{img}', confidence=0.7)
            moveRandom(current_img)
            pyautogui.click()
            pyautogui.sleep(1.3)
            print('found!!', img)
            break
        except:
            print('not found')


def gear_up():
    try:
        axe = pyautogui.locateOnScreen('images/tools/bAxeBank.png', confidence=0.8)
        knife = pyautogui.locateOnScreen('images/tools/knifeBank.png', confidence=0.8)

        moveRandom(knife)
        pyautogui.click()
        pyautogui.sleep(1)
        
        moveRandom(axe)
        pyautogui.click()
        pyautogui.sleep(1)

        axe = pyautogui.locateOnScreen('images/tools/bAxeInv.png', confidence=0.8)
        moveRandom(axe)

        pyautogui.keyDown('shift')
        pyautogui.click()
        pyautogui.keyUp('shift')

    except:
        print('ERROR')


def varrock_trees():
    bond = pyautogui.locateOnScreen('images/misc/map-bond.png', confidence=0.9)
    print(bond)
    pyautogui.moveTo(bond.left+25, bond.top-5, duration=0.5)
    pyautogui.click()
    pyautogui.sleep(4.5)
    pyautogui.click()
    

# # FINDING TREES

haystack = cv2.imread('images/trees/haystack2.png', cv2.IMREAD_UNCHANGED)

treedle = cv2.imread('images/trees/treedle4.png', cv2.IMREAD_UNCHANGED)

# cv2.imshow('haystack', haystack)
# cv2.waitKey()
# cv2.destroyAllWindows()

# cv2.imshow('treedle', treedle)
# cv2.waitKey()
# cv2.destroyAllWindows()

result = cv2.matchTemplate(haystack, treedle, cv2.TM_CCOEFF_NORMED)

# cv2.imshow('result', result)
# cv2.waitKey()
# cv2.destroyAllWindows()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_loc, max_val)
w = treedle.shape[1]
h = treedle.shape[0]
print(w, h)
cv2.rectangle(haystack, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,0), 2)

# cv2.imshow('haystack', haystack)
# cv2.waitKey()
# cv2.destroyAllWindows()
# pyautogui.moveTo(316, 262)

threshold = 0.3
yloc, xloc = np.where(result >= threshold)
print(len(xloc))

rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

for (x, y, w, h) in rectangles:
    cv2.rectangle(haystack, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('haystack', haystack)
# cv2.waitKey()
# cv2.destroyAllWindows()






# setCamera()
# bank()
# pyautogui.sleep(2)
# gear_up()
# pyautogui.sleep(1)
# varrock_trees()