import cv2
import mediapipe as mp
import time


class FaceMeshDetector():
    def __int__(self, staticMode=False, maxFaces=1, minDetectionCon=0.5, minTrackingCon=0.5):
        self.results = None
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackingCon = minTrackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.minDetectionCon,
                                                 self.minTrackingCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(imgRGB)
        faces = []

        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS,
                                           self.drawSpec, self.drawSpec)

        face = []
        for id, lm in enumerate(faceLms.landmarks):
            ih, iw, ic = img.shape
            x, y = int(lm.x * iw), int(lm.y * ih)
            cv2.putText(img, str(id), (x, y),
                        cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 2)

            face.append([x, y])
        faces.append(face)
        return img, faces


def main():
    capture = cv2.VideoCapture("Videos/1.mp4")
    pTime = 0
    detector = FaceMeshDetector(maxFaces=2)

    while True:
        success, img = capture.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(faces[0])

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.imshow("Image", img)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()
