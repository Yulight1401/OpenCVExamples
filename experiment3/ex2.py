import cv2

import numpy as np

img=cv2.imread('../images/child.jpg',0)

rows,cols=img.shape

M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)


dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite('img.png',dst)

cv2.imshow('img',dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
