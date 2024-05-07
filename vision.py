import cv2 as cv
import numpy as np

class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        # SIZE OF NEEDLE IMG
        self.needle_h = self.needle_img.shape[0]
        self.needle_w = self.needle_img.shape[1]

        self.method = method

    
    def find(self, haystack_img, threshold=0.5, debug_mode=None):
    
        # FOUND BEST RESULTS WERE CCOEFF_NORMED HERE
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)


        # GETS THE BEST MATCHED POSITION
        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print("best matchests top-left pos: ", max_loc, "best match confidence: ", max_val)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print('Found ', len(locations), 'locations')

        # GROUPING RECTANGLES AND REMOVING OVERLAP
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

        points = []
        if len(rectangles):
            # print('found needle')

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

                    # CONVERT HAYSTACK INTO READABLE IMG FOR RECTANGLE
                    haystack_img = np.array(haystack_img)
                    # haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)

                    # DRAWING THE BOX
                    cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

                elif debug_mode == 'points':
                    cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)
            
        if debug_mode:
            cv.imshow('Matches', haystack_img)
            # cv.waitKey()

        return points