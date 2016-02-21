import numpy as np
import cv2
import random

def main():

    img = cv2.imread('/Users/Nolan/Documents/theGreenGoal2.png')
    img2 = cv2.imread('/Users/Nolan/Documents/theGreenGoal2.png')
    imgToMatch = cv2.imread('/Users/Nolan/Documents/frcGOAL.png')
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    cv2.imwrite("/Users/Nolan/Documents/theMask.png", mask)

    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imwrite("/Users/Nolan/Documents/theRES.png", res)

    edges = cv2.Canny(res,50,150,apertureSize = 3)
    edges1 = cv2.Canny(imgToMatch,50,150,apertureSize = 3)

    cv2.imwrite("/Users/Nolan/Documents/theEdges.png", edges)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
    contours1, hierarchy1 = cv2.findContours(edges1, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

    goalNum = 0
    contour1 = contours1[1]

    potGoalSpot = []
    potGoalNum = []

    for i in range(0, len(contours)):
        contour = contours[i]
        M = cv2.moments(contour)
        if M['m00'] <= 50:
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
        potGoalSpot.append(i)
        potGoalNum.append(matching)
        print(matching, i)
        
    print("************Potential goal at spot ", potGoalSpot[min(xrange(len(potGoalNum)),key=potGoalNum.__getitem__)], " and with number ", min(potGoalNum))

    whitePixels = 0

    contour = contours[potGoalSpot[min(xrange(len(potGoalNum)),key=potGoalNum.__getitem__)]]
    cv2.drawContours(img2, contours, potGoalSpot[min(xrange(len(potGoalNum)),key=potGoalNum.__getitem__)], [0, 0, 255], 5)

    cv2.imwrite("/Users/Nolan/Documents/theContors.png", img)
    cv2.imwrite("/Users/Nolan/Documents/theContorsWithOne.png", img2)

if __name__ == '__main__':
    main()
