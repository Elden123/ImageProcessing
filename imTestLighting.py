import numpy as np
import time

print("loading...")
time.sleep(2)

cap = cv2.VideoCapture(0)

_, frame = cap.read()

cv2.imwrite("/Users/Nolan/Documents/theFrameTesting.png", frame)


# define range of blue color in HSV
lower_blue = np.array([240,240,240])
upper_blue = np.array([255,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(frame, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imwrite("/Users/Nolan/Documents/theColorTesting.png", res)
print("done.")