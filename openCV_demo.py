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







### indexing, slicing, and iterating numpy arrays ###
first_two_rows = grey_image[0:2]
print(first_two_rows)

two_rows_and_two_columns = grey_image[0:2, 2:4]
print(two_rows_and_two_columns)

shape = grey_image.shape
print(shape) # prints the dimensions of the image, in this case (3, 5)

for row in grey_image:
    print(row)

for column in grey_image.T:
    print(column)

for pixel in grey_image.flat:
    print(pixel)







### stacking and splitting numpy arrays ###
horizontal_array = numpy.hstack((grey_image, grey_image, grey_image, grey_image)) # horizontally stack arrays, pass in a tuple
print(horizontal_array)
cv2.imwrite("horizontal_array.png", horizontal_array)

vertical_array = numpy.vstack((grey_image, grey_image, grey_image, grey_image))
cv2.imwrite("veritacal_array.png", vertical_array)

split_arrays = numpy.hsplit(vertical_array, 5)
print(split_arrays)
