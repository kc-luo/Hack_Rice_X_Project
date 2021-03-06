import cv2
import numpy as np
from helper import *
from ISR.predict import Predictor
from ISR.models import RDN
from ISR.models import RRDN
from PIL import Image

class Transformer:
    def __init__(self, model, weight, sharpen=True, sharp_first=False, sharp_strong=False):
        """
        model, an instance of ISR.models
        weight, an string which is the path of weight to be loaded
        """
        self.expander = model.model.load_weights(weight)
        if not sharpen:
            self.func = lambda x: model.predict(x)
        elif sharp_first:
            self.func = lambda x: model.predict(sharp(x, sharp_strong))
        else:
            self.func = lambda x: sharp(model.predict(x), sharp_strong)
    
    def predict(self, x):
        return self.func(x)

    