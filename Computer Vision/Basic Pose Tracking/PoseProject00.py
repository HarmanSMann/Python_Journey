import cv2
import time
import PoseEstimationModule as pem


capture = cv2.VideoCapture('video/2.mp4')  # this should capture whatever video you want to analyze
pTime = 0
detector = pem.poseDetector()

while True:
    success, img = capture.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        cv2.circle(img, (lmList[11][1], lmList[11][2]), 10, (0, 255, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
