import cv2
import numpy as np

BASE_URL = '../images/'
img = cv2.imread(BASE_URL + 'child.jpg')
cv2.namedWindow('image')
cv2.imshow('image', img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindow()
elif key == ord('s'):
    cv2.imwrite('newimg.png', img)
    cv2.destroyAllWindows()
