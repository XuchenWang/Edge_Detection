'''
  File name: edgeLink.py
  Author: Xuchen Wang
  Date created: Sept 17, 2019
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents the final canny edge detection map
'''

import numpy as np
import interp
import matplotlib.pyplot as plt
from findDerivatives import findDerivatives
from nonMaxSup import nonMaxSup
import utils
from PIL import Image


def edgeLink(M, Mag, Ori):

# set the high and low threshold
    highThresholdRatio = 2.5
    lowThresholdRatio = 1.1
    Mag1 = np.copy(Mag)
    highThreshold = np.mean(M*Mag1)*highThresholdRatio
    lowThreshold = np.mean(M*Mag1)*lowThresholdRatio

# construct the next edge points' coordinate
    x,y = np.meshgrid(np.arange(Mag.shape[1]), np.arange(Mag.shape[0]))

    new_ori = np.tan(-1/(np.tan(Ori)+0.0001))
    x_pri = x+np.cos(new_ori)
    y_pri = y+np.sin(new_ori)
    X_pri = x-np.cos(new_ori)
    Y_pri = y-np.sin(new_ori)

# iterating until no further high threshold edge is detected
    oldNumOne=0
    numOne=0.1
    while(oldNumOne!=numOne):
        oldNumOne = numOne

        Mag_point1 = interp.interp2(Mag1,x_pri,y_pri)
        Mag_point2 = interp.interp2(Mag1,X_pri,Y_pri)



        Mag1 = np.where((M==1) & (Mag1>=highThreshold),highThreshold,
                        np.where((M==1) & (Mag1>=lowThreshold)
                                 &((Mag_point1>=highThreshold) |
                                   (Mag_point2>=highThreshold)),
                                 highThreshold,Mag1))


        numOne = np.sum(Mag1==highThreshold)
    E = np.where(Mag1 == highThreshold,1,0)
    # plt.imshow(E, cmap='gray')
    # plt.show()
    return E


# #Testing edgeLink
# I = np.array(Image.open('123.jpg').convert('RGB'))
# I_gray = utils.rgb2gray(I)
# plt.imshow(I_gray, cmap='gray', vmin=0, vmax=255)
# plt.show()
# Mag, Magx, Magy, Ori = findDerivatives(I_gray)
# M = nonMaxSup(Mag, Ori)
# E = edgeLink(M, Mag, Ori)
#
