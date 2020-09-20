import cv2
import numpy as np
from helper import *
from ISR.predict import Predictor
from ISR.models import RDN
from ISR.models import RRDN
from PIL import Image
from transformer import Transformer
from progressbar import *

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
            width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)*2)
            height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)*2)
            length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
        else :
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)*2)
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)*2)
            length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # print(fps)
        dim = (width, height)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        new_path = path[:len(path) - 4] + "_enhanced.mp4"
        out = cv2.VideoWriter(new_path, fourcc, fps, dim)
        
        i = 0
        progress = ProgressBar().start()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame = self.p.predict(frame)
            # write the flipped frame
            out.write(frame)
            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
            i += 1
            progress.update(int(i / length * 100))

        progress.finish()
        cap.release()
        cv2.destroyAllWindows()