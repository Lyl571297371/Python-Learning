import os
from PIL import Image
from pylab import *
from numpy import *

def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))
    
    return array(pil_im.resize(sz))
