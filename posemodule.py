import cv2
import mediapipe as mp
import math

class PoseDetector:
    """
    Estimates Pose points of a human body using the mediapipe library.
    """
    def __init__(self, mode=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param upBody: Upper boy only flag
        :param smooth: Smoothness Flag
        :param detectionCon: Minimum Detection Confidence Threshold
        :param trackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,
                                     smooth_landmarks=self.smooth,
                                     min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence=self.trackCon)

    def findPose(self, img, draw=True):
        """
        Find the pose landmarks in an Image of BGR color space.
        :param img: Image to find the pose in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy,])

            # Bounding Box
            ad = abs(self.lmList[12][1] - self.lmList[11][1]) // 2

            if draw:
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return self.lmList

    def findleg(self, img, p1, p2, p3, draw=True):

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Calculate the Angle
        leg = (math.degrees(math.atan2(x3 - y1, y1 - x2) -
                            math.atan2(x3 - y2, y2 - x2)))

        if leg >= 10:
            leg += 60

        # Draw
        if draw:
            cv2.circle(img, (x1, y1), 1, (10, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 1, (0, 0, 255),2)
            cv2.circle(img, (x2, y2), 1, (10, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 1, (0, 0, 255),2)
            cv2.circle(img, (x3, y3), 1, (10, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 1, (0, 0, 255),2)
            cv2.putText(img, str(int(leg)), (x2 - 50, y2 + 50),
                      cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            return leg
    def findtrunk(self, img, p1, p2, p3, draw=True):

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        trunk =(math.degrees(math.atan2(x2 -y1, y3 - x2) -
                             math.atan2(x3 - y3, y2- x2)))

        if trunk >=20:
            trunk+=0

        if draw:
            #cv2.circle(img, (x1, y1), 1, (10, 0, 255), cv2.FILLED)
            #cv2.circle(img, (x1, y1), 1, (0, 0, 255),2)
            #cv2.circle(img, (x2, y2), 1, (10, 0, 255), cv2.FILLED)
            #cv2.circle(img, (x2, y2), 1, (0, 0, 255),2)
            #cv2.circle(img, (x3, y3), 1, (10, 0, 255), cv2.FILLED)
            #cv2.circle(img, (x3, y3), 1, (0, 0, 255),2)
            ##         cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            return trunk

    def findwrist (self, img, p1, p2, p3, draw=True):

            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            x3, y3 = self.lmList[p3][1:]

            # Calculate the Angle
            wrist = (math.degrees(math.atan2(x3 - y1, y1 - x2) -
                                math.atan2(x3 - y2, y2 - x2)))

            if wrist >= 10:
                wrist += 0

            # Draw
            if draw:
              #  cv2.circle(img, (x1, y1), 1, (10, 0, 255), cv2.FILLED)
              ## cv2.circle(img, (x2, y2), 1, (10, 0, 255), cv2.FILLED)
               # cv2.circle(img, (x2, y2), 1, (0, 0, 255), 2)
               # cv2.circle(img, (x3, y3), 1, (10, 0, 255), cv2.FILLED)
               # cv2.circle(img, (x3, y3), 1, (0, 0, 255), 2)
               # cv2.putText(img, str(int(wrist)), (x2 - 50, y2 + 50),
               #             cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                return wrist

    def findneck(self, img, p1, p2, p3, draw=True):

            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            x3, y3 = self.lmList[p3][1:]

            # Calculate the Angle
            neck = (math.degrees(math.atan2(x3- y2, x1 - y1) -
                                math.atan2(x3- y3, x3 - y1)))

            if neck <=40:
                neck += 0

            # Draw
            if draw:
                #cv2.circle(img, (x1, y1), 1, (10, 0, 255), cv2.FILLED)
                #cv2.circle(img, (x1, y1), 1, (0, 0, 255), 2)
                #cv2.circle(img, (x2, y2), 1, (10, 0, 255), cv2.FILLED)
                #cv2.circle(img, (x2, y2), 1, (0, 0, 255), 2)
                #cv2.circle(img, (x3, y3), 1, (10, 0, 255), cv2.FILLED)
                ###          cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                return neck

    def lowerarm(self, img, p1, p2, p3, draw=True):

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Calculate the Angle
        lowerarm = (math.degrees(math.atan2(x2 - y2, y3 - x2) -
                              math.atan2(x2 - y3, y1 - x2)))

        if lowerarm >= 0:
            lowerarm += 20

        # Draw
        if draw:
           # cv2.circle(img, (x1, y1), 1, (10, 0, 255), cv2.FILLED)
           # cv2.circle(img, (x1, y1), 1, (0, 0, 255), 2)
           ## cv2.circle(img, (x2, y2), 1, (0, 0, 255), 2)
           # cv2.circle(img, (x3, y3), 1, (10, 0, 255), cv2.FILLED)
           # cv2.circle(img, (x3, y3), 1, (0, 0, 255), 2)
           # cv2.putText(img, str(int(lowerarm)), (x2 - 50, y2 + 50),
            #            cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            return lowerarm

    def upperarm(self, img, p1, p2, p3, draw=True):

            x1, y1 = self.lmList[p1][1:]
            x2, y2 = self.lmList[p2][1:]
            x3, y3 = self.lmList[p3][1:]

            upperarm = (math.degrees(math.atan2(x1 - y2, x2 - y1) -
                                  math.atan2(x3 - y2, x1 - y2)))

            if upperarm >= 20:
                upperarm += 0

            # Draw
            if draw:
                cv2.circle(img, (x1, y1), 1, (10, 0, 255), cv2.FILLED)
                cv2.circle(img, (x1, y1), 1, (0, 0, 255), 2)
                cv2.circle(img, (x2, y2), 1, (10, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 1, (0, 0, 255), 2)
                cv2.circle(img, (x3, y3), 1, (10, 0, 255), cv2.FILLED)
                cv2.circle(img, (x3, y3), 1, (0, 0, 255), 2)
                cv2.putText(img, str(int(upperarm)), (x2 - 50, y2 + 50),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                return upperarm

def main():
    cap = cv2.VideoCapture("video/2.mp4")
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
        if bboxInfo:
            center = bboxInfo["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "_main_":
    main()