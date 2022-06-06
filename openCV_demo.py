# docs: https://opencv.org/

import numpy
import cv2

### turn an image into a numpy array ###
grey_image = cv2.imread("smallgray.png", 0)
print(grey_image)
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]





### turn a numpy array into an image ###
cv2.imwrite("new_image.png", grey_image)