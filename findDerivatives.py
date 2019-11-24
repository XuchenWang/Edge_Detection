'''
  File name: findDerivatives.py
  Author: Xuchen Wang
  Date created: Sept 12, 2019
'''

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import scipy.signal as signal
import utils

'''
  File clarification:
    Compute gradient information of the input grayscale image
    - Input I_gray: H x W matrix as image
    - Output Mag: H x W matrix represents the magnitude of derivatives
    - Output Magx: H x W matrix represents the magnitude of derivatives along x-axis
    - Output Magy: H x W matrix represents the magnitude of derivatives along y-axis
    - Output Ori: H x W matrix represents the orientation of derivatives
'''

def findDerivatives(I_gray):

## ==========Filter out noise
    img = ndimage.gaussian_filter(I_gray, sigma=1.5, order=0)
    # plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    # plt.show()

## ==========Compute derivative
    dx, dy = np.gradient(utils.GaussianPDF_2D(0, 0.5, 5, 5), axis = (1,0))
    Ix = signal.convolve2d(img,dx,'same')
    Iy = signal.convolve2d(img,dy,'same')
    # plt.imshow(Ix, cmap='gray')
    # plt.show()
    # plt.imshow(Iy, cmap='gray')
    # plt.show()

## ==========Compute the magnitude
    Mag = np.sqrt(Ix*Ix + Iy*Iy);
    # plt.imshow(Mag, cmap='gray')
    # plt.show()

## =========Compute orientation
    Ori = np.arctan2(Iy, Ix+0.0001)


    return Mag, Ix, Iy, Ori






# #Testing finDerivatives
# I = np.array(Image.open('48017.jpg').convert('RGB'))
# I_gray = utils.rgb2gray(I)
# # plt.imshow(I_gray, cmap='gray', vmin=0, vmax=255)
# # plt.show()
# findDerivatives(I_gray)









