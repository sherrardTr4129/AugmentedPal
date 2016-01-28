import cv2
import numpy as np
  
class Effects(object):
    
    def render(self, CSH, hammer, other ,image, axisBot, axisTop, axisCol, axisS1, axisS2, axisS3, axisS4, axisS5, axisH1, axisH2):
  
        # load calibration data
        with np.load('webcam_calibration_ouput.npz') as X:
            mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
  
        # set up criteria, object points and axis
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
          
        objp = np.zeros((6*7,3), np.float32)
        objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
  
        # find grid corners in image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (7,9), None)

  
        if ret == True:
            cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            rvecs, tvecs, _ = cv2.solvePnPRansac(objp, corners, mtx, dist)
	    if CSH == True:
                # project 3D points to image plane
            	imgpts, _ = cv2.projectPoints(axisBot, rvecs, tvecs, mtx, dist)
            	imgpts1, _ = cv2.projectPoints(axisTop, rvecs, tvecs, mtx, dist)
            	imgpts2, _ = cv2.projectPoints(axisCol, rvecs, tvecs, mtx, dist)
            	imgpts3, _ = cv2.projectPoints(axisS1, rvecs, tvecs, mtx, dist)
            	imgpts4, _ = cv2.projectPoints(axisS2, rvecs, tvecs, mtx, dist)
            	imgpts5, _ = cv2.projectPoints(axisS3, rvecs, tvecs, mtx, dist)
            	imgpts6, _ = cv2.projectPoints(axisS4, rvecs, tvecs, mtx, dist)
            	imgpts7, _ = cv2.projectPoints(axisS5, rvecs, tvecs, mtx, dist)
            	imgpts8, _ = cv2.projectPoints(axisH1, rvecs, tvecs, mtx, dist)
            	imgpts9, _ = cv2.projectPoints(axisH2, rvecs, tvecs, mtx, dist)

  
            	# draw cube
            	self._draw_cube(image, imgpts)
            	self._draw_cube(image, imgpts1)
            	self._draw_cube(image, imgpts2)
	    	self._draw_cube(image, imgpts3)
	    	self._draw_cube(image, imgpts4)
	    	self._draw_cube(image, imgpts5)
	    	self._draw_cube(image, imgpts6)
	    	self._draw_cube(image, imgpts7)
	    	self._draw_cube(image, imgpts8)
	    	self._draw_cube(image, imgpts9)
	    	return image
	    elif hammer == True:
            	imgptsOther, _ = cv2.projectPoints(other, rvecs, tvecs, mtx, dist)
            	self._draw_cube(image, imgptsOther)
		return image
    def _draw_cube(self, img, imgpts):
        imgpts = np.int32(imgpts).reshape(-1,2)
  
        # draw floor
        cv2.drawContours(img, [imgpts[:4]],-1,(0,0,0),3)
  
        # draw pillars
        for i,j in zip(range(4),range(4,8)):
            cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(0),3)
  
        # draw roof
        cv2.drawContours(img, [imgpts[4:8]],-1,(0,0,0),3)
	return img
    
