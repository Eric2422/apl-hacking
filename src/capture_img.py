from datetime import datetime
import sys

import cv2

if len(sys.argv) < 2:
    raise ValueError('Passs in either "positive" or "negative"')

if sys.argv[2] != 'positive' and sys.argv[2] != 'negative':
    raise ValueError('Passs in either "positive" or "negative"')

write_dir = sys.argv[2]

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
    cv2.imwrite(f'./{write_dir}/{datetime.now()}.jpg', gray)

    # Wait one millisecond and return the key pressed
    key = cv2.waitKey(1)

    # 27 is the ASCII code for escape
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
capture.release()
