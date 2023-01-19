'//how to object recognition in real time camera?'  
import numpy as np
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

URL = 'http://25.251.55.246:8080/video'
cap = cv2.VideoCapture(URL)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect objects and draw on screen
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox( bbox, label, conf)

    cv2.imshow('output',output_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


