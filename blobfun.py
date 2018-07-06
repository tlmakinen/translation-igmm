# playing around with blob detection in .czi files

import numpy as np
from skimage.filters import gaussian
import matplotlib.pyplot as plt
import tifffile
import pyqtgraph as pg
import czifile  # for reading the microscope file
from filtering import czi_gauss

import cv2

smoothczi = czi_gauss('testfile.czi', sigma=0.4)
smoothim = smoothczi.smoothed_im 

img = smoothim[10,3,:,:]   # take a slice of the 3D temporal image to play with

cv2.imwrite('blobslice.jpeg',img)
#pg.image(img)

im = cv2.imread('blobslice.jpeg', cv2.IMREAD_GRAYSCALE)  # read image

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)