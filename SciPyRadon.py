import os.path
import math
import numpy as np

import scipy.interpolate
import scipy.misc
import scipy.ndimage.interpolation
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def testInput(N, filename):
    assert type(N) is int, "N is not an integer: %r" % N  
    assert os.path.isfile(filename), "%r does not exist" % filename  
    
def angle(i): 
    return (math.pi*i)/N

N = input("Please Enter the number of projections: ")
filename = raw_input("Please Enter Phantom File Name: ")

testInput(N, filename);

phantom = scipy.misc.imread(filename)

plt.imshow(phantom, cmap=cm.Greys_r)
plt.title('Shepp-Logan Phantom')
plt.show()

sinogram = np.zeros(256);

#rotationAngle = angle(0);
#rotatedPhantom = scipy.ndimage.interpolation.rotate(phantom, np.rad2deg(rotationAngle), order = 3, reshape = False, mode = 'constant', cval = 0.0);
projectionView = np.sum(phantom, axis=0);

for i in xrange(256):
	sinogram[i] = projectionView[i];

for i in xrange(1, N):
    rotationAngle = angle(i);
    rotatedPhantom = scipy.ndimage.interpolation.rotate(phantom, np.rad2deg(rotationAngle), order = 3, reshape = False, mode = 'constant', cval = 0.0);
    projectionView = np.sum(rotatedPhantom, axis=0);
    sinogram = np.vstack((sinogram, projectionView));

output = raw_input("Please enter an Output File name: ");
scipy.misc.imsave(output, sinogram)

plt.imshow(sinogram, cmap=cm.Greys_r)
plt.title('Complete Sinogram')
plt.show()