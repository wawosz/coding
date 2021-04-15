#
# Sample Python script to illustrate Python capabilities to
# calculate various textural (heterogeneity) parameters
#
# For analysis a simulated image was used - heterogenous image defined as
# array (30x30 matrix)
#

# STANDARD MODULES IMPORT
# if not installed, execute the following commands:
# pip install numpy
# pip install matplotlib
# pip install scipy
# pip install scikit-image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
from skimage.feature import greycomatrix, greycoprops

# create a random heterogenous image array (30x30)
# with pixel values 0 - 256
# For textural analysis images need to be converted to int16
simulated_image = 256 * np.random.rand(30, 30)
A = simulated_image.astype(np.int16)

# convert simulated heterogenous test image to gray levels values
glcm_A = greycomatrix(A, [5], [0], 256, symmetric=True, normed=True)
sliced_A = glcm_A[:256, :256, 0, 0]  # need 256x256 array for plotting GLCM

# Calculate various heterogeneity parameters (contrast, orderliness, energy and variance)
# CONTRAST GROUP
Diss_A = greycoprops(glcm_A, 'dissimilarity')[0, 0]
Corr_A = greycoprops(glcm_A, 'correlation')[0, 0]
Homo_A = greycoprops(glcm_A, 'homogeneity')[0, 0]
Cont_A = greycoprops(glcm_A, 'contrast')[0, 0]
# ORDERLINESS GROUP
ASM_A = greycoprops(glcm_A, 'ASM')[0, 0]
Energy_A = greycoprops(glcm_A, 'energy')[0, 0]
# calculate image variance
V_A = ndimage.variance(A)

# Plot simulated array
plt.figure(1)
plt.imshow(A, cmap='gray', interpolation='bicubic') #bicubic interpolation makes image more smooth
plt.title('Heterogenous image')
plt.colorbar()

# Plot processed simulated array (needed for calculation of heterogeneity parameters)
plt.figure(2)
plt.imshow(sliced_A, cmap='gray_r', interpolation='bicubic')
plt.title('GLCM for heterogenous image')
plt.colorbar()

plt.show()


# Print calculated parameters
print('Heterogenous Image')
print('===========================')
print('Variance =', V_A)
print('Dissimilarity =', Diss_A)
print('Correlation =', Corr_A)
print('Contrast =', Cont_A)
print('Homogeneity =', Homo_A)
print('Angular Second Moment (ASM) =', ASM_A)
print('Energy (or Uniformity) =', Energy_A)
