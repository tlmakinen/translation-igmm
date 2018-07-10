# create a blob helper type to make finding translation regions easier
import numpy as np
from skimage.filters import gaussian
import matplotlib.pyplot as plt
import tifffile
import pyqtgraph as pg
import czifile  # for reading the microscope file
from filtering import czi_gauss

class blob:
    def __init__(self):
        self.x = []   # create empty lists of pixels
        self.y = []
        self.z = []

    def add_pixel(self, x, y, z):   # define a method to add pixels to blob object
        self.x.append(x)
        self.y.append(y)
        self.z.append(z)
    
    def mass(self):
        self.mass = len(self.x) # return the length of the x array -- equivalent to the number of pixels
                               # (x,y,z) added to the blob
        
    def center_of_mass(self):
        self.xcom = (np.sum(self.x)) / self.mass
        self.ycom = (np.sum(self.y)) / self.mass
        self.zcom = (np.sum(self.z)) / self.mass

        self.com_coord = [self.xcom, self.ycom, self.zcom]

    # def distanceTo(self,blob):
