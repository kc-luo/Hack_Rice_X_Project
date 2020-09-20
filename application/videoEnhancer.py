import cv2
import numpy as np
from helper import *
from ISR.predict import Predictor
from ISR.models import RDN
from ISR.models import RRDN
from PIL import Image
from transformer import Transformer

class VideoEnhancer:
    def __init__(self, transformer):
        """
        transformer, an instance of class transformer
        """
        self.p = transformer
        

    def enhance(self, path):
        """
        path, a string which is the path of video

        Returns None
        Saves the enhanced video of mp4 format in the same directory
        """
        cap = cv2.VideoCapture(path)
        # Get fps & resolution of original video
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        if int(major_ver)  < 3 :
            fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
            width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        else :
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(fps)
        dim = (width, height)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        new_path = path[:len(path) - 4] + "_enhanced.mp4"
        out = cv2.VideoWriter(new_path, fourcc, fps, dim)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame = self.p.predict(frame)
            # write the flipped frame
            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()