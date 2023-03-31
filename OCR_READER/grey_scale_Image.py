import cv2

"""
    Grayscale is a preprocessing layer that transforms RGB images to Grayscale images.
    Input images should have values in the range of [0, 255]. (src : https://keras.io/api/keras_cv/layers/preprocessing/grayscale/)

    This is done because the grey scaled images are compressed to minimal pixels.
    Thus, it enhance visualization.
"""


def grayscale(image):
    # cvtColor :- To convert the image from one colour space to another.
    # COLOR_BGR2GRAY :- RBG to grey scaled.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("temp/gray.jpg", gray_image)
    # Path of the grey scaled images is returned.
    return gray_image
