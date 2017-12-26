import numpy as np
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('../videos/output.avi', fourcc, 20.0, (640, 480))
while(1):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        cv2.putText(frame,'OpenCV',(10,500), font, 4,(255,255,255),2)
        out.write(frame)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
