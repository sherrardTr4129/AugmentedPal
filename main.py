import cv2
from detection import Detection
from render import Effects
import numpy as np



detect = Detection()
cap = cv2.VideoCapture(0)
ren = Effects()
axisBase = np.float32([[0,0,0], [0,8,0], [2,8,0], [2,0,0],[0,0,-1],[0,8,-1],[2,8,-1],[2,0,-1]])
axisTop = np.float32([[0,0,-10], [0,8,-10], [2,8,-10], [2,0,-10],[0,0,-12],[0,8,-12],[2,8,-12],[2,0,-12]])
axisCol = np.float32([[0,0,-1], [0,2,-1], [2,2,-1], [2,0,-1],[0,0,-10],[0,2,-10],[2,2,-10],[2,0,-10]])
axisS1 = np.float32([[0,3,-7], [0,6,-7], [2,6,-7], [2,3,-7],[0,3,-8],[0,6,-8],[2,6,-8],[2,3,-8]])
axisS2 = np.float32([[0,3,-5], [0,4,-5], [2,4,-5], [2,3,-5],[0,3,-7],[0,4,-7],[2,4,-7],[2,3,-7]])
axisS3 = np.float32([[0,3,-5], [0,6,-5], [2,6,-5], [2,3,-5],[0,3,-6],[0,6,-6],[2,6,-6],[2,3,-6]])

while True:
     ret, frame = cap.read()
     ren.render(frame, axisBase, axisTop, axisCol, axisS1, axisS2, axisS3)
     cv2.imshow("frame", frame)
     cv2.waitKey(1)

