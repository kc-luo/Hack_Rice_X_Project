import cv2
import numpy as np


def sharp(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.floqat32)
    dst = cv2.filter2D(image, -1, kernel=kernel)
    return (dst)


vid = cv2.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    sharpen = sharp(frame)
    numpy_horizontal = np.hstack((frame, sharpen))
    cv2.imshow('Numpy Horizontal', numpy_horizontal)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()