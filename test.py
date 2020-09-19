import numpy as np
from PIL import Image
import os

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ISR.models import RDN

rdn = RDN(weights='psnr-small')

img3 = Image.open('E:\_Kevin\Code\Hack_Rice_X_Project\sample\\baboon.png')
# lr_img3 = np.array(img3)
# hr_img3 = Image.fromarray(lr_img3)
# tf.keras.preprocessing.image.save_img("test.png", hr_img3)