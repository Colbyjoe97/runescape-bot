import pyautogui
from main import setCamera
import random
import os
import cv2 as cv
import numpy as np
# import win32gui, win32ui, win32con

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

def findClickPositions(needle_img_path, haystack_img_path, threshold=0.5, debug_mode=None):

    # GETTINGS IMAGES
    haystack = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    treedle = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

    # SIZE OF NEEDLE IMG
    needle_h = treedle.shape[0]
    needle_w = treedle.shape[1]


    # FOUND BEST RESULTS WERE CCOEFF_NORMED HERE
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack, treedle, cv.TM_CCOEFF_NORMED)

    # GETS THE BEST MATCHED POSITION
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("best matchests top-left pos: ", max_loc, "best match confidence: ", max_val)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    print('Found ', len(locations), 'locations')

    # GROUPING RECTANGLES AND REMOVING OVERLAP
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    points = []
    if len(rectangles):
        print('found needle')

        # dimensions of needle img
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS
        
        for (x, y, w, h) in rectangles:

            # GETTING CERNTER POSITION
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)

            # SAVING THE POINTS
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
            
                # FINDING BOX POSITIONS
                top_left = (x, y)
                bottom_right = (x + w, y + h)

                # DRAWING THE BOX
                cv.rectangle(haystack, top_left, bottom_right, line_color, line_type)

            elif debug_mode == 'points':
                cv.drawMarker(haystack, (center_x, center_y), marker_color, marker_type)
        
        if debug_mode:
            cv.imshow('Matches', haystack)
            cv.waitKey()

        return points


points = findClickPositions('images/trees/copper.png', 'images/trees/minestack.png', debug_mode='points')
print(points)

rectangles = findClickPositions('images/trees/copper.png', 'images/trees/minestack.png', debug_mode='rectangles')
print(rectangles)




# setCamera()
# bank()
# pyautogui.sleep(2)
# gear_up()
# pyautogui.sleep(1)
# varrock_trees()