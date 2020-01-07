#
# Sample Python script to illustrate Python capabilities to
# calculate various textural (heterogeneity) parameters
#
# Two type of images were used: heterogenous image defined as
# array (30x30 matrix) and an image sample (30x30 matrix)
# downloaded from internet (FDG PET tumor image)
#

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
from skimage.feature import greycomatrix, greycoprops

# load a representative image for heterogeneity analysis
img = mpimg.imread('sample.tif')

# for testing image rotation and its effect on textural parameters
# org_img = mpimg.imread('sample.tif')
# img = ndimage.rotate(org_img, 90)

# create a random heterogenous image array (30x30)
# with pixel values 0 - 256
# For textural analysis images need to be converted to int16
simulated_image = 256 * np.random.rand(30, 30)
A = simulated_image.astype(np.int16)

# convert sample homogenous tumor image to gray level values
glcm_img = greycomatrix(img, [5], [0], 256, symmetric=True, normed=True)
sliced_img = glcm_img[:256, :256, 0, 0]  # need 256x256 array for plotting GLCM

# convert simulated heterogenous test image to gray levels values
glcm_A = greycomatrix(A, [5], [0], 256, symmetric=True, normed=True)
sliced_A = glcm_A[:256, :256, 0, 0]  # need 256x256 array for plotting GLCM

# CONTRAST GROUP
Diss_img = greycoprops(glcm_img, 'dissimilarity')[0, 0]
Diss_A = greycoprops(glcm_A, 'dissimilarity')[0, 0]

Corr_img = greycoprops(glcm_img, 'correlation')[0, 0]
Corr_A = greycoprops(glcm_A, 'correlation')[0, 0]

Homo_img = greycoprops(glcm_img, 'homogeneity')[0, 0]
Homo_A = greycoprops(glcm_A, 'homogeneity')[0, 0]

Cont_img = greycoprops(glcm_img, 'contrast')[0, 0]
Cont_A = greycoprops(glcm_A, 'contrast')[0, 0]

# ORDERLINESS GROUP
ASM_img = greycoprops(glcm_img, 'ASM')[0, 0]  # Angular Second Moment
ASM_A = greycoprops(glcm_A, 'ASM')[0, 0]

Energy_img = greycoprops(glcm_img, 'energy')[0, 0]  # named also as Uniformity
Energy_A = greycoprops(glcm_A, 'energy')[0, 0]

# calculate image variance
V_A = ndimage.variance(A)
V_img = ndimage.variance(img)

# plot representative figures
plt.figure(1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.title('Homogenous image')
plt.colorbar()

plt.figure(2)
plt.imshow(sliced_img, cmap='nipy_spectral', interpolation='bicubic')
plt.title('GLCM for homogenous image')
plt.colorbar()

plt.figure(3)
plt.imshow(A, cmap='gray', interpolation='bicubic')
plt.title('Heterogenous image')
plt.colorbar()

plt.figure(4)
plt.imshow(sliced_A, cmap='nipy_spectral', interpolation='bicubic')
plt.title('GLCM for heterogenous image')
plt.colorbar()

plt.show()


# show calculated parameters
print('Homogenous Image')
print('===========================')
print('Variance =', V_img)
print('Dissimilarity =', Diss_img)
print('Correlation =', Corr_img)
print('Contrast =', Cont_img)
print('Homogeneity =', Homo_img)
print('Angular Second Moment (ASM) =', ASM_img)
print('Energy (or Uniformity) =', Energy_img)
print()
print('Heterogenous Image')
print('===========================')
print('Variance =', V_A)
print('Dissimilarity =', Diss_A)
print('Correlation =', Corr_A)
print('Contrast =', Cont_A)
print('Homogeneity =', Homo_A)
print('Angular Second Moment (ASM) =', ASM_A)
print('Energy (or Uniformity) =', Energy_A)
