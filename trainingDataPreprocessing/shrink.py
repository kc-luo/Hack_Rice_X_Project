import cv2 as cv
import os

def shrink(file):
    img = cv.imread(file, 1)

    width = int(img.shape[1] * 0.5)
    height = int(img.shape[0] * 0.5)
    dim = (width, height)

    half = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    cv.imwrite(file[:8]+"x2.jpg", half)


for dirpath, dirnames, files in os.walk('img', topdown=False):
    for file_name in files:
        shrink("img/" + file_name)