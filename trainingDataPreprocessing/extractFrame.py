import cv2 as cv
import os

def capture(file):
    cap = cv.VideoCapture(file)
    i = 1
    j = 0

    interval = 900

    while (cap.isOpened()):
        cap.set(1, j)
        ret, frame = cap.read()
        if ret == False:
            break
        cv.imwrite("img/" + "{:04d}".format(i) + ".jpg", frame)
        i += 1
        j += interval

    cap.release()
    cv.destroyAllWindows()


for dirpath, dirnames, files in os.walk('vid', topdown=False):
    for file_name in files:
        capture("vid/"+file_name)
