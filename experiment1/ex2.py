import cv2
vcap = cv2.VideoCapture()
import numpy as np
import time


vcap.open('../videos/videoa.avi')
ret, frame = vcap.read()
while(ret):
    cv2.imshow("capture", frame)
    # get a frame
    ret, frame = vcap.read()
    # show a frame
    time.sleep(0.02)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vcap.release()
cv2.destroyAllWindows()
