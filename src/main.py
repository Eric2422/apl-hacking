from datetime import datetime
import sys

from ultralytics import YOLO
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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', gray)

    # Wait one millisecond and return the key pressed
    key = cv2.waitKey(1)

    # 27 is the ASCII code for escape
    if key == 27:
        break

cv2.destroyAllWindows()
capture.release()
