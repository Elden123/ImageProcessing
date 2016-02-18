import numpy as np
import cv2
import random

def main():
    img = cv2.imread('/Users/Nolan/Documents/2016.jpg')
    img2 = cv2.imread('/Users/Nolan/Documents/frcGOAL.jpg')
    imgToMatch = cv2.imread('/Users/Nolan/Documents/frcGOAL.png')

    # define range of blue color in HSV
    lower_blue = np.array([240,240,240])
    upper_blue = np.array([255,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    edges = cv2.Canny(res,50,150,apertureSize = 3)
    edges1 = cv2.Canny(imgToMatch,50,150,apertureSize = 3)

    cv2.imwrite("/Users/Nolan/Documents/theEdges.png", edges)
    cv2.imwrite("/Users/Nolan/Documents/theFrcEdges.png", edges1)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
    contours1, hierarchy1 = cv2.findContours(edges1, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

    goalNum = 0
    
    contour1 = contours1[1]

    cv2.imwrite("/Users/Nolan/Documents/theFrcGoal.png", imgToMatch)

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
        matching = cv2.matchShapes(contour1,contour,1,0.0)
        print(matching, i)
        if matching <= 8.0:
            print("*************************GOAL*************************")
            goalNum += 1

    if goalNum >= 2:
        print("Oops! ", goalNum, " goals were found")

    whitePixels = 0
    
    cv2.imwrite("/Users/Nolan/Documents/theContors.png", img)

if __name__ == '__main__':
    main()
