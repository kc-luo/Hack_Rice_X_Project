import cv2 as cv
import os

def capture(str):
    cap = cv.VideoCapture(str)
    i = 1
    j = 0

    interval = 900

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if (j%interval==0):
            cv.imwrite("img/" + "{:04d}".format(i) + ".jpg", frame)
            i += 1
        j += 1
    cap.release()
    cv.destroyAllWindows()


for dirpath, dirnames, files in os.walk('vid', topdown=False):
    for file_name in files:
        capture("vid/"+file_name)
