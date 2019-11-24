'''
  File name: nonMaxSup.py
  Author: Xuchen Wang
  Date created: Sept 15, 2019
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''
import numpy as np
import interp
import matplotlib.pyplot as plt
from findDerivatives import findDerivatives
import utils
from PIL import Image

def nonMaxSup(Mag, Ori):

# Construct interpolation for upper point and lower point
    x,y = np.meshgrid(np.arange(Mag.shape[1]), np.arange(Mag.shape[0]))
    x_pri = x+np.cos(Ori)
    y_pri = y+np.sin(Ori)
    Mag_point1 = interp.interp2(Mag,x_pri,y_pri)
    X_pri = x-np.cos(Ori)
    Y_pri = y-np.sin(Ori)
    Mag_point2 = interp.interp2(Mag,X_pri, Y_pri)



# Compare three matrices: Mag, Mag_point1, Mag_point2
# Only when Mag > Mag_point1 and Mag > Mag_point2, M=1
# if replace 1 with Mag, we will get a picture looks like Mag, but thinner
    M = np.where((Mag>Mag_point1) & (Mag>Mag_point2),1,0)
    # plt.imshow(M, cmap='gray')
    # plt.show()

    return M


# #Testing nonMaxSup
# I = np.array(Image.open('48017.jpg').convert('RGB'))
# I_gray = utils.rgb2gray(I)
# # plt.imshow(I_gray, cmap='gray', vmin=0, vmax=255)
# # plt.show()
# Mag, Magx, Magy, Ori = findDerivatives(I_gray)
# M = nonMaxSup(Mag, Ori)

