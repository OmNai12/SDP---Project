import cv2
from grey_scale_Image import grayscale
from black_white_Image import black_AND_white
from resizeImage import display
# from matplotlib import pyplot as plt


def ocr_Function(path: str):
    img = cv2.imread(path)

    # Note :- Step 1 and 2 are part of the binarization of an image.

    ### Step :- 1
    # Grey scalling the image.
    grey_scaled_Image = grayscale(img)
    # Displaying the grey scaled image.
    # display(grey_scaled_Image)

    ### Step :- 2
    # Converting to black and white image.
    black_white_Image = black_AND_white(grey_scaled_Image)
    # Displaying black and white image.
    # display(black_white_Image)
    pass


if __name__ == "__main__":
    path = "data/img_test.png"
    ocr_Function(path)
