import cv2
from grey_scale_Image import grayscale
from black_white_Image import black_AND_white
from noise_removal_Image import noise_removal
from border_remove_Image import remove_borders
from PIL import Image
import pytesseract
# from resizeImage import display
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

    ### Step :- 3
    # Removing the noise from the image.
    noise_removed_Image = noise_removal(black_white_Image)
    # Displaying noise removed image.
    # display(noise_removed_Image)

    ### Step :- 4
    # Removing the borders.
    border_removed_Image = remove_borders(noise_removed_Image)
    # Displaying border removed images.

    ### Step :- 5
    # Text from image
    final_Image = Image.open("temp/no_borders.jpg")
    ocr_Output = pytesseract.image_to_string(final_Image)
    return ocr_Output


if __name__ == "__main__":
    path = "data/img_test.png"
    text = ocr_Function(path)
    print(text)
