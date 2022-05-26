import cv2
import os
import time
import HandTrackingModule as htm

##########################################
wCam, hCam = 640, 480
##########################################

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
# create a folder that holds images of finger counts

folderPath = "FingerImages"
myList = os.listdir(folderPath)
# print(myList)
overlayList = []
for inPath in myList:
    image = cv2.imread(f'{folderPath}/{inPath}')
    # print(f'{folderPath}/{inPath}')
    overlayList.append(image)

# print(len(overlayList))

detector = htm.handDetector()
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    # print(lmlist)

    if len(lmlist) != 0:
        fingers = []
        # thumb
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)

        totalFingers = fingers.count(1)
        print(totalFingers)

        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers-1]  # size of image

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
