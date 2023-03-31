import cv2
from matplotlib import pyplot as plt
from imageFit import display

# Opening Image

image_file = "page_01.png"
img = cv2.imread(image_file)
# Title to be passed and the image captured.
# this will not fit the screen size so by matplot we adjust it.
# cv2.imshow("original image", img)
# cv2.waitKey(0)

# To rezie the image
# display(image_file)


# 1. Invert the images
# Exatly opposite of the current pixel value
# eg white to black.
# inverted_image = cv2.bitwise_not(img)
# cv2.imwrite("temp/inverted.jpg", inverted_image)
# display("temp/inverted.jpg")

# 2. Binarization
# Otimal size of the image file.

def greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


grey_image = greyscale(img)
cv2.imwrite("temp/grey.jpg", grey_image)
# display("temp/grey.jpg")
# # To set the threshold
thresh, im_bw = cv2.threshold(grey_image, 200, 300, cv2.THRESH_BINARY)
cv2.imwrite("temp/bw_image.jpg", im_bw)
display("temp/bw_image.jpg")

#
