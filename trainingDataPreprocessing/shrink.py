import cv2 as cv
import os

def shrink(file):
    img = cv.imread(file, 1)

    width = int(img.shape[1] * 0.5)
    height = int(img.shape[0] * 0.5)
    dim = (width, height)
    # print(file)
    file_id = file.split("/")[-1]
    # print(file_id)
    file_id = file_id[:len(file_id) - 4]
    # print(file_id)
    half = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    cv.imwrite("./trainingDataPreprocessing/img_x/" + file_id + "x2.png", half)


for dirpath, dirnames, files in os.walk('./trainingDataPreprocessing/img_y', topdown=False):
    for file_name in files:
        shrink("./trainingDataPreprocessing/img_y/" + file_name)