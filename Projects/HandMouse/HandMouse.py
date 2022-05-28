import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy


##########################################
wCam, hCam = 640, 480
wScr, hScr = autopy.screen.size()
frameR = 100
smoothingVal = 7
##########################################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0


cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)


detector = htm.HandTrackingModule(maxHands=1)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()
        cv2.rectangel(img, (frameR, frameR), (wCam-frameR,
                      hCam - frameR), (255, 0, 255), 2)
        cv2.rectangel(img, (frameR, frameR), (wCam-frameR,
                      hCam - frameR), (255, 0, 255), 2)

        # move motion
        if fingers[1] == 1 and fingers[2] == 0:

            x3 = np.interp(x1, (0, wCam), (0, wScr))
            y3 = np.interp(y1, (0, hCam), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothingVal
            clocY = plocY + (y3 - plocY) / smoothingVal

            autopy.mouse.move(wScr-x3, y3)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # click mode
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (400, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
