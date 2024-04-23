import pyautogui
import random
import os


# UNIVERSAL FUNCTIONS
def moveRandom(img):
    x = random.random()*-img.width
    y = random.random()*-img.height
    pyautogui.moveTo((img.left-x), (img.top-y), duration=0.5)


# FINDING BANKER
startPath = 'images/banker'
img_list = os.listdir(startPath)
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
        axe = pyautogui.locateOnScreen('images/tools/bAxeBank.png', confidence=0.9)

        x = random.random()*-axe.width
        y = random.random()*-axe.height
        pyautogui.moveTo((axe.left-x), (axe.top-y), duration=0.5)
        pyautogui.click()

        pyautogui.sleep(1)

        axe = pyautogui.locateOnScreen('images/tools/bAxeInv.png', confidence=0.9)
        x = random.random()*-axe.width
        y = random.random()*-axe.height
        pyautogui.moveTo((axe.left-x), (axe.top-y), duration=0.5)
        pyautogui.hold('shift')
        pyautogui.click()

    except:
        print('ERROR')






bank()
pyautogui.sleep(2)
gear_up()