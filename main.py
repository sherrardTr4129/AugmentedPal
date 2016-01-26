import cv2
from detection import Detection
from render import Effects



detect = Detection()
cap = cv2.VideoCapture(0)
ren = Effects()
while True:
     ret, frame = cap.read()
     #detect.is_item_detected_in_image("faceDetection.xml", frame)
     ren.render(frame)
     cv2.imshow("frame", frame)
     cv2.waitKey(1)

