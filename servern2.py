import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture("http://192.168.0.113:8000/stream.mjpg")

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist, bbox = detector.findPosition(img)
    print(bbox)
    #{'bbox': (313, -64, 140, 425), 'center': (383, 148)}
    if (bbox):
        cv2.circle(img, (bbox['center'][0], bbox['center'][1] - 15), 5, (0,0,255))
    cv2.imshow("Out", img)
    cv2.waitKey(1)

cv2.destroyAllWindows()