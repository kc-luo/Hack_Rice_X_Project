import cv2 as cv
import os


i = 1
def capture(file, interval=900):
    cap = cv.VideoCapture(file)
    length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    global i
    j = 0

    while (cap.isOpened() and j < length):
        cap.set(1, j)
        ret, frame = cap.read()
        if ret == False:
            break
        cv.imwrite("./trainingDataPreprocessing/img_y/" + "{:04d}".format(i) + ".png", frame)
        i += 1
        j += interval

    cap.release()
    cv.destroyAllWindows()


for dirpath, dirnames, files in os.walk('./trainingDataPreprocessing/vid', topdown=False):
    for file_name in files:
        capture("./trainingDataPreprocessing/vid/" + file_name)
