import pyautogui
import random

# GENERAL USE
# fullHealth = pyautogui.locateOnScreen('images/full-health.png', confidence=0.8)

# bArrows = pyautogui.locateOnScreen('images/bronze-arrows.png', confidence=0.8)
# bShield = pyautogui.locateOnScreen('images/bshield.png', confidence=0.8)
# bSword = pyautogui.locateOnScreen('images/bsword2.png', confidence=0.8)

# print(fullHealth)
# print(bShield)
# print(pyautogui.center(fullHealth))

# FUNCTIONS
# gear = [bShield, bArrows]
# gear = [bArrows, bShield, bSword]
def equip():
    for slot in gear:
        print(slot)
        x = random.random()*-slot.width
        y = random.random()*-slot.height
        pyautogui.moveTo((slot.left-x), (slot.top-y), duration=0.3)
        # pyautogui.rightClick()
        # equip = pyautogui.locateCenterOnScreen('images/equip.png', confidence=0.6)
        # pyautogui.moveTo(equip, duration=0.3)
        # pyautogui.click()

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
    