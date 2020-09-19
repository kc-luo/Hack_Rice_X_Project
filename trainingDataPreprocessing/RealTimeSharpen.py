import cv2
import numpy as np


def sharp(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.floqat32)
    dst = cv2.filter2D(image, -1, kernel=kernel)
    #cv2.imwrite("img\demo.png", dst)
    return (dst)


#src = cv2.imread("/Users/jiaqilu/Desktop/321_test.png")
#sharp(src)

vid = cv2.VideoCapture(0)
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    #cv2.imshow('image',frame)

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