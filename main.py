import cv2
from detection import Detection
from render import Effects
import numpy as np



detect = Detection()
cap = cv2.VideoCapture(0)
ren = Effects()
axisBase = np.float32([[0,0,0], [0,6,0], [2,6,0], [2,0,0],[0,0,-1],[0,6,-1],[2,6,-1],[2,0,-1]])
axisTop = np.float32([[0,0,-9], [0,6,-9], [2,6,-9], [2,0,-9],[0,0,-10],[0,6,-10],[2,6,-10],[2,0,-10]])
axisCol = np.float32([[0,0,-1], [0,1,-1], [2,1,-1], [2,0,-1],[0,0,-9],[0,1,-9],[2,1,-9],[2,0,-9]])
axisS1 = np.float32([[0,2,-7], [0,5,-7], [2,5,-7], [2,2,-7],[0,2,-8],[0,5,-8],[2,5,-8],[2,2,-8]])
axisS2 = np.float32([[0,2,-5], [0,3,-5], [2,3,-5], [2,2,-5],[0,2,-7],[0,3,-7],[2,3,-7],[2,2,-7]])
axisS3 = np.float32([[0,2,-5], [0,5,-5], [2,5,-5], [2,2,-5],[0,2,-6],[0,5,-6],[2,5,-6],[2,2,-6]])
axisS4 = np.float32([[0,4,-3], [0,5,-3], [2,5,-3], [2,4,-3],[0,4,-5],[0,5,-5],[2,5,-5],[2,4,-5]])
axisS5 = np.float32([[0,2,-3], [0,5,-3], [2,5,-3], [2,2,-3],[0,2,-4],[0,5,-4],[2,5,-4],[2,2,-4]])
axisH1 = np.float32([[0,6,-5], [0,7,-5], [2,7,-5], [2,6,-5],[0,6,-6],[0,7,-6],[2,7,-6],[2,6,-6]])
axisH2 = np.float32([[0,7,0], [0,8,0], [2,8,0], [2,7,0],[0,7,-10],[0,8,-10],[2,8,-10],[2,7,-10]])


while True:
     ret, frame = cap.read()
     ren.render(frame, axisBase, axisTop, axisCol, axisS1, axisS2, axisS3, axisS4, axisS5, axisH1, axisH2)
     cv2.imshow("frame", frame)
     cv2.waitKey(1)

