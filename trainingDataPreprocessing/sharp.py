import cv2 as cv
import numpy as np


def sharp(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imwrite("img\demo.png", dst)


src = cv.imread("img\\test.png")
sharp(src)
