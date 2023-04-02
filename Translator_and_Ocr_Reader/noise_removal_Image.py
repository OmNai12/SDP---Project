import cv2
import numpy as np

"""
Image denoising is to remove noise from a noisy image, so as to restore the true image.
However, since noise, edge, and texture are high frequency components,
it is difficult to distinguish them in the process of denoising and the denoised images could inevitably lose some details.
Overall, recovering meaningful information from noisy images in the process,
of noise removal to obtain high quality images is an important problem nowadays. (src : https://vciba.springeropen.com/)

Thus, it removes the grains genrated in the image, both present in the image and genrated due to the binarization.
"""

# Note :- Black and white image to be passed.


def noise_removal(image):
    # kernal is of dim :- Used for the edge detection of the image.
    kernel = np.ones((1, 1), np.uint8)
    # dilate :- It increasses the thikness of the characters based on the morphological criteria provided the given kernal.
    no_noise = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 2), np.uint8)
    # erode :- It decreasses the thikness of the characters based on the morphological criteria provided the given kernal.
    no_noise = cv2.erode(no_noise, kernel, iterations=1)
    # morphologyEx :- Given morphological criteria based on the given neighbours it takes the action.
    no_noise = cv2.morphologyEx(no_noise, cv2.MORPH_CLOSE, kernel)
    # medianBlur :- Bluring the image to the given scale.
    no_noise = cv2.medianBlur(no_noise, 3)
    cv2.imwrite("temp/no_noise.jpg", no_noise)
    return (no_noise)
