import sys

import numpy as np
import cv2

# Get input from camera
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print('Failed...')
    sys.exit()

print('Camera running...')

while True:
    # Get status and frame from camera
    cap_return, frame = capture.read()

    if not cap_return:
        print('Failed to retrieve frame')
        continue

    lower_bound = (30, 0, 0)
    upper_bound = (100, 255, 255)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mat1 = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    out_frame = cv2.bitwise_and(frame, frame, mask=mat1)

    cv2.imshow('frame', out_frame)

    # Wait one millisecond and return the key pressed
    key = cv2.waitKey(1)

    # 27 is the ASCII code for escape
    if key == 27:
        break

cv2.destroyAllWindows()
capture.release()
