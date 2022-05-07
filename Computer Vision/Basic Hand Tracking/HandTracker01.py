import cv2
import mediapipe as mp
import time

# The value set in here is used for the which camera you plan to use, if you have multiple
capture = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.proccess(imgRGB)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
