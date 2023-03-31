import cv2

"""
This transformation is useful in detecting blobs and further reduces the computational complexity.
The critical task is to find a suitable threshold. (src : https://www.dynamsoft.com/)
"""

# Note : grey scaled image to be passed.


def black_AND_white(image):
    # threshold :- For every pixel, the same threshold value is applied...
    # If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value.
    # THRESH_BINARY :- dst(x,y) = { (maxValue, if src(x,y)>thresh), (0, otherwise)
    thresh, img_bw = cv2.threshold(image, 205, 275, cv2.THRESH_BINARY)
    cv2.imwrite("temp/bw_image.jpg", img_bw)
    return img_bw
