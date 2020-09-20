import cv2 as cv
import numpy as np

default_kernel
def sharp(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    return dst

if __name__ == "__main__":
    src = cv.imread("img\\test.png")
    sharp(src)
