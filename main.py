import cv2
from detection import Detection
from render import Effects
import numpy as np



detect = Detection()
cap = cv2.VideoCapture(0)
ren = Effects()
axisBase = np.float32([[0,0,0], [0,8,0], [2,8,0], [2,0,0],[0,0,-1],[0,8,-1],[2,8,-1],[2,0,-1]])
axisTop = np.float32([[0,0,-6], [0,8,-6], [2,8,-6], [2,0,-6],[0,0,-7],[0,8,-7],[2,8,-7],[2,0,-7]])
axisCol = np.float32([[0,0,-1], [0,2,-1], [2,2,-1], [2,0,-1],[0,0,-6],[0,2,-6],[2,2,-6],[2,0,-6]])
while True:
     ret, frame = cap.read()
     ren.render(frame, axisBase, axisTop, axisCol)
     cv2.imshow("frame", frame)
     cv2.waitKey(1)

