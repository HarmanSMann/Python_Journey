import cv2
import mediapipe as mp
import time

"""
ids:
0 - wrist
1 - Thumb cmc
2 - Thumb mcp
3 - Thumb ip
4 - Thumb tip
5 - index mcp
6 - index pip
7 - index dip
8 - index tip
9 - middle mcp
10 - middle pip
11 - middle dip
12 - middle tip
13 - ring mcp
14 - ring pip
15 - ring dip
16 - ring tip
17 - pinky mcp
18 - pinky pip
19 - pinky dip
20 - pinky tip
"""

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cTime = 0
pTime = 0


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # detect the hand
    # print(result.multi_hand_landmarks)
    # Create a scanner to indicate and show what the camera is scanning
    if results.multi_hand_landmarks:
        for handLMs in results.multi_hand_landmarks:
            for id, lm in enumerate(handLMs.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                
                 # this will highlight specificly the index tip
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            # Draw a connection point between each dot
            mpDraw.draw_landmarks(img, handLMs, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # place a fps counter to show how many refreshes are happening
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)


if __name__ == "__main__":
    main()
