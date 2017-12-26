REACTANGLE_SIZE = 20
STEP = 10

import cv2
import numpy as np
import matplotlib.pyplot as plt

path ='../images/flower123.jpg'
lwpImg = cv2.imread(path)
gray_lwpImg = cv2.cvtColor(lwpImg, cv2.COLOR_BGR2GRAY)

lwpImg = cv2.rectangle(lwpImg, (290, 0), (310, 327), (0, 255, 0), 2)
cv2.imshow('local_pixel', lwpImg)

pixel_data = np.array(gray_lwpImg)
box_data = pixel_data[:, 290:310]
pixel_sum = np.sum(box_data, axis=1)

x = range(200)
fig = plt.figure(figsize=(4, 2))
ax1 = fig.add_subplot(1, 1, 1)
ax1.bar(x, pixel_sum, width=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('edge_filter')
plt.grid(True)
plt.show()

key = cv2.waitKey(0) & 0xFF
if key == ord('q'):
    cv2.destroyAllWindows()
