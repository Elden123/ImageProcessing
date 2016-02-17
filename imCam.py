import numpy as np
import cv2
import random

def main():
    img = cv2.imread('/Users/Nolan/Documents/2016_MED.jpg')
    img2 = cv2.imread('/Users/Nolan/Documents/frcGOAL.jpg')


    # define range of blue color in HSV
    lower_blue = np.array([240,240,240])
    upper_blue = np.array([255,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    edges = cv2.Canny(res,50,150,apertureSize = 3)

    cv2.imwrite("/Users/Nolan/Documents/theEdges.png", edges)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

    for i in range(0, len(contours)):
        contour = contours[i]
        M = cv2.moments(contour)
        if M['m00'] <= 300:
            continue
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        area = str(M['m00'])
        b = random.randint(128, 255)
        g = random.randint(128, 255)
        r = random.randint(128, 255)
        cv2.drawContours(img, contours, i, [b, g, r], 5)
        cv2.putText(img, area,(cx, cy), cv2.FONT_HERSHEY_SIMPLEX, .5,(r, g, b),2)

    whitePixels = 0

    
    cv2.imwrite("/Users/Nolan/Documents/theContors.png", img)

    #for h in range(0, 2987):
     #   for w in range(0, 5311):
      #      if not np.all([res[h, w], [0,0,0]]):
        #        whitePixels += 1
         #       print( whitePixels )
          #      isGoal(h, w, res)  

def isGoal(height, width, img):
    white = []
    whiteCount = 0
    for w in range(width, width + 250):
        if not np.all([img[height, w], [0,0,0]]):
            white.append(1)
        else:
            white.append(0)
    for l in white:
        if white[l] == 1:
            whiteCount = whiteCount + 1
    if whiteCount >= 230:
        white = []
        for i in range(height, height + 100):
            if not np.all([img[100, 100], [0,0,0]]):
                white.append(1)
            else:
                white.append(0)
        whiteCount = 0
        for j in white:
            if white[j] == 1:
                whiteCount = whiteCount + 1
        if whiteCount >= 50:
            print("*************GOAL**************")

if __name__ == '__main__':
    main()
