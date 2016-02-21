import numpy as np
import cv2
import random
import time

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
time.sleep(3)
retval, img = camera.read()

cv2.imwrite("/Users/Nolan/Documents/theGreenGoal2.png", img)