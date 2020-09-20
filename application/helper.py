import cv2 as cv
import os
import numpy as np

def bicub(img):
    width = int(img.shape[1] * 2)
    height = int(img.shape[0] * 2)
    dim = (width, height)
    return cv.resize(img, dim, interpolation=cv.INTER_CUBIC)


def sharp(image, is_strong=False):
    if is_strong:
        kernel = np.array([[-1, -1, 0], [-2, 5, -2], [0, 1, 1]], np.float32)
    else:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    return dst