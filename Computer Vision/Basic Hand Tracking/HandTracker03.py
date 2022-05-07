import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands()
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[8])  # throw the id of whatever you want to print

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
