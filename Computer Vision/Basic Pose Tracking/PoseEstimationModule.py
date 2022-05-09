import cv2
import mediapipe as mp
import time


class poseDetector():
    def __init__(self, mode=False, complexity=1, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.results = None
        self.mode = mode
        self.complexity = complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        # There has been an update, now complexity is required for this to run
        self.pose = self.mpPose.Pose(
            self.mode, complexity, self.upBody, self.smooth, self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRBG)
        if self.results.pose_landmarks:
            self.mpDraw.draw_landmarks(
                img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
        return lmList


def main():
    # this should capture whatever video you want to analyze
    capture = cv2.VideoCapture('video/2.mp4')
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = capture.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:
            cv2.circle(img, (lmList[11][1], lmList[11]
                       [2]), 10, (0, 255, 0), cv2.FILLED)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
