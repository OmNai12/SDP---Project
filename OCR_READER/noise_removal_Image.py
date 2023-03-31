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


def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)
