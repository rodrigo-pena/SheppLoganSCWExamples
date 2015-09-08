# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:07:24 2015

@author: rodrigopena

Rotation Based Projector 

"""

#%% Import libraries

import math
import numpy as np

import scipy.interpolate
import scipy.misc
import scipy.ndimage.interpolation

#%% Open the image file

phantom = scipy.misc.imread("Phantom.jpg")

#%% Setup variables
angle = 0.5
n_projections = 180 / angle
image = np.copy(phantom)

#%% Loop on the number of projections
for p in range(int(n_projections)):

    #%% Rotate the image
    rotatedImage = scipy.ndimage.interpolation.rotate(image, angle, order=3, 
                                                      reshape=False, 
                                                      mode='constant',
                                                      cval=0.0)
    
    #%% Sum across columns
    imageSum = np.sum(rotatedImage, axis=0)
    
    #%% Stack projection views
    if p == 0:
        sinogram = np.copy(imageSum)
    else:
        sinogram = np.vstack((sinogram, imageSum))
    
    #%% Set current rotation as the next image
    image = np.copy(rotatedImage)
    
#%% Save resulting image
    
# Normalize
sinogram = sinogram.astype('float')
sinogram -= np.min(sinogram.ravel())
sinogram /= np.max(sinogram.ravel())
sinogram *= 255

scipy.misc.imsave("Sinogram.jpg", sinogram)