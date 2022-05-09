import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

capture = cv2.VideoCapture('video/2.mp4') # this should capture whatever video you want to analyze
pTime = 0

while True:
    success, img = capture.read()
    # The video is in BGR, but the mediapipe uses RGB so we have to convert it
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRBG)

    # inorder to get some information out of the result try this
    # print(results.pose_landmarks)
    # this will print out the points (the dots) for a person and the connections

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # this step is used because the x and y of the id is et with correlation to the image size as a percentage , so an image was on the right side in the center, it could be set as: .90, .50
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
