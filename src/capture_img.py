from datetime import datetime
import sys

import cv2

try:
    write_dir = sys.argv[1]

    if sys.argv[1] != 'positive' and sys.argv[1] != 'negative':
        raise ValueError()

except IndexError | ValueError:
    raise ValueError('Passs in either "positive" or "negative"')



# Get input from camera
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print('Failed...')
    sys.exit()

print('Camera running...')

# When True, write images
capture_images = False

while True:
    # Get status and frame from camera
    cap_return, frame = capture.read()

    if not cap_return:
        print('Failed to retrieve frame')
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    
    print(f'Currently{' ' if capture_images else ' *NOT* '}recording.')

    if capture_images:
        cv2.imwrite(f'./{write_dir}/{datetime.now()}.jpg', gray)

    # Wait one millisecond and return the key pressed
    key = cv2.waitKey(1)

    match int(key):
        # 27 is the ASCII code for escape
        # 113 is the code for "q"
        case int(27 | 113):
            break

        # Start/stop capturing when spacebar is hit
        # 32 is the code for " "(spacebar)
        case 32:
            capture_images = not capture_images

cv2.destroyAllWindows()
capture.release()
