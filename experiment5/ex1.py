
import numpy as np
from matplotlib import pyplot as plt
import cv2

BASE_URL = '../images/'

img = cv2.imread(BASE_URL + 'girl.jpg')
blur = cv2.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
