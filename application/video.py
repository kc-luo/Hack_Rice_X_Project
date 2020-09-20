import numpy as np
from ISR.models import RDN
from ISR.models import RRDN
from PIL import Image
from transformer import Transformer
from videoEnhancer import VideoEnhancer

rdn = RDN(arch_params={'C':3, 'D':10, 'G':64, 'G0':64, 'x':2})
weight_pre = './weights/rdn-C3-D10-G64-G064-x2_epoch140.hdf5'
weight_tuned = './weights/rdn-C3-D10-G64-G064-x2_best-val_generator_loss_epoch142.hdf5'

p_pre = Transformer(rdn, weight_tuned, True, False, False)
enhancer = VideoEnhancer(p_pre)
path = "./videos/video_3_360p.mp4"
enhancer.enhance(path)