import numpy as np
from skimage.filters import gaussian
import tifffile
import pyqtgraph as pg
import czifile  # for reading the microscope file

class czi_gauss:
    def __init__(self, fname, sigma):
        im = czifile.imread(fname)

        im = np.squeeze(im)  # get rid of 1D labels
        
        smooth_im = []
        for i in range(len(im[:,1,1,1])):
            smooth_im.append(gaussian(im[i,:,:,:], sigma=0.4, multichannel=False))
        smooth_im = np.asarray(smooth_im)




