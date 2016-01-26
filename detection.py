import cv2
 
class Detection(object):
 
    def is_item_detected_in_image(self, item_cascade_path, image):
  
        # do detection
        item_cascade = cv2.CascadeClassifier(item_cascade_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        items = item_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=36)
 
        for (x,y,w,h) in items:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                
        # indicate whether item detected in image
        return len(items) > 0
