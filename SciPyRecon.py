import os.path
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import scipy.interpolate
import scipy.fftpack
import scipy.misc
import scipy.ndimage.interpolation

def sqr(x): return x * x

def testInput(N, filename):
    assert os.path.isfile(filename), "%r does not exist" % filename  
	   
    
def angle(i): 
    return (math.pi*i)/N

filename = raw_input("Please Enter Sinogram File Name: ")

testInput(N, filename);

sinogram = scipy.misc.imread(filename)

N, S = sinogram.shape

sinogram_fft_rows=scipy.fftpack.fftshift(
scipy.fftpack.fft(
scipy.fftpack.ifftshift(sinogram, 
axes = 1
)
), 
axes=1)

a = np.array([angle(i) for i in xrange(N)])
r = np.arange(S) - S/2;
r, a = np.meshgrid(r, a);
r = r.flatten();
a = a.flatten();
srcx = (S/2)+r*np.cos(a)
srcy = (S/2)+r*np.sin(a)

dstx, dsty = np.meshgrid(np.arange(S), np.arange(S))
dstx = dstx.flatten()
dsty = dsty.flatten()

fft2 = scipy.interpolate.griddata(
(srcy, srcx), sinogram_fft_rows.flatten(), 
(dsty, dstx),
method='cubic',
fill_value=0.0
).reshape((S, S))

recon = np.real(scipy.fftpack.fftshift(
scipy.fftpack.ifft2(
scipy.fftpack.ifftshift(fft2))))

scipy.misc.imsave('Recon.jpg', recon)