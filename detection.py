import numpy as np
import cv2


class Detection(object):
     def Detect(self, Haar1, Haar2, img):
         cascade1 = cv2.CascadeClassifier(Haar1)
         cascade2 = cv2.CascadeClassifier(Haar2)
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         item1 = cascade1.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (50,50))
         item2 = cascade2.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (50,50))
         for (x,y,w,h) in item1:
              cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
         for (x,y,w,h) in item2:
              cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
         if(len(item1) == 0 and len(item2) == 0):
              return False, False
         else:
	      return len(item1) > 0, len(item2) > 0

