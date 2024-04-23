import pyautogui
from main import setCamera
import random
import os
import cv2

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
treeList = 'images/trees/varrock/normal'
allTrees = os.listdir(treeList)
for tree in allTrees:
    print(tree)
    try:
        testPath = r'images/trees/varrock/normal/'+tree 
        this_cvTree = cv2.imread(testPath)
        # print(this_cvTree)

        this_pyTree = pyautogui.locateOnScreen(f'images/trees/varrock/normal/{tree}', confidence=0.8, )
        print(this_pyTree)
        
        # rect = cv2.rectangle(this_pyTree, (this_pyTree.top,this_pyTree.left), (this_pyTree.top-10,this_pyTree.left+10), (0,0,0), -1)
        # rect = cv2.rectangle(this_cvTree, (5,5), (220,220), (0,255,0), 2)
        rect = cv2.rectangle(this_cvTree, (5,5), (this_pyTree.width-5,this_pyTree.height-5), (0,255,0), 2)
        
        cv2.imshow(window_name, rect)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # moveRandom(this_tree)
    except:
        print(f'TREE NOT FOUND')


# test2 = pyautogui.locateOnScreen('images/trees/varrock/normal/normal2.png', confidence=0.8)
# print(test)
# cv2.rectangle(test,(test2.top, test2.left),(test2.top-50,test2.right+50),(0,0,255),5)


# setCamera()
# bank()
# pyautogui.sleep(2)
# gear_up()
# pyautogui.sleep(1)
# varrock_trees()