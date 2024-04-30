import cv2 as cv
import numpy as np
import pyautogui
from main import setCamera
import random
import os


def findClickPositions(needle_img_path, haystack_img_path, threshold=0.5, debug_mode=None):

    # GETTINGS IMAGES
    haystack = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    ore = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

    # SIZE OF NEEDLE IMG
    needle_h = ore.shape[0]
    needle_w = ore.shape[1]


    # FOUND BEST RESULTS WERE CCOEFF_NORMED HERE
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack, ore, cv.TM_CCOEFF_NORMED)

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


points = findClickPositions('images/resources/ore/copper.png', 'images/resources/ore/minestack.png', debug_mode='points')
print(points)

rectangles = findClickPositions('images/resources/ore/copper.png', 'images/resources/ore/minestack.png', debug_mode='rectangles')
print(rectangles)