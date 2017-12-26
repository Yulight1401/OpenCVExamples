import cv2
import numpy as np
img = cv2.imread('../images/flower123.jpg',0)
source = cv2.imread('../images/flower123.jpg',0)
# cv2.imshow('source', img)
print(img.shape)
size = 32
for row in range(0, img.shape[0] - size):
	for col in range(0, img.shape[1] - size):
			temp_img = img[row : row + size,col : col + size]
			equ = cv2.equalizeHist(temp_img)
			img[row + int(size / 2)][col + int(size / 2)] = equ[int(size / 2)][int(size / 2)]
res = np.hstack((source, img))
cv2.imshow('dst', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
