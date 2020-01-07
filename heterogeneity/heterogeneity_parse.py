#  Script reads predefined files in a directory and
#  outputs heterogeneity results as CVS file
# 

import os
import glob
import numpy as np
import tkinter as tk
# import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
from skimage.feature import greycomatrix, greycoprops
from tkinter import filedialog


# define colors to be used in string variables and printing text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


root = tk.Tk()
root.withdraw()

# open window and request the active directory where images are located
path = filedialog.askdirectory(parent=root, initialdir=os.getcwd(),
                                       title='Please select a directory')

# print in blue color selected path
print(bcolors.OKBLUE + "Current path: " + path + bcolors.ENDC)

# list specific files (here jpg in selected path)
results = np.array(['File number', 
                    'Filename',
                    'Dissimilarity',
                    'Correlation',
                    'Homogeneity',
                    'Contrast',
                    'ASM',
                    'Energy',
                    'Variance'])
n = 1
for filename in glob.glob(os.path.join(path, '*.tif')):
    print(str(n), filename)
    # load image for heterogeneity analysis
    img = mpimg.imread(filename)
    
    # convert the image to gray level values
    glcm_img = greycomatrix(img, [5], [0], 256, symmetric=True, normed=True)
    # need 256x256 array for plotting and saving GLCM
    sliced_img = glcm_img[:256, :256, 0, 0]
    new_filename = filename + '_glcm.png'
    mpimg.imsave(new_filename, arr=sliced_img) 

    # CONTRAST GROUP
    Diss_img = greycoprops(glcm_img, 'dissimilarity')[0, 0]
    Corr_img = greycoprops(glcm_img, 'correlation')[0, 0]
    Homo_img = greycoprops(glcm_img, 'homogeneity')[0, 0]
    Cont_img = greycoprops(glcm_img, 'contrast')[0, 0]
    # ORDERLINESS GROUP
    ASM_img = greycoprops(glcm_img, 'ASM')[0, 0]  # Angular Second Moment
    Energy_img = greycoprops(glcm_img, 'energy')[0, 0]  # Uniformity
    # IMAGE VARIANCE
    V_img = ndimage.variance(img)

    # show calculated parameters
    print('Variance =', V_img)
    print('Dissimilarity =', Diss_img)
    print('Correlation =', Corr_img)
    print('Contrast =', Cont_img)
    print('Homogeneity =', Homo_img)
    print('Angular Second Moment (ASM) =', ASM_img)
    print('Energy (or Uniformity) =', Energy_img)
    print('===========================')
    print()

    # append data to results array
    results = np.append(results, [n, filename, Diss_img,
                                  Corr_img, Homo_img, Cont_img,
                                  ASM_img, Energy_img, V_img])

    # next file index
    n = n + 1

# SAVE RESULTS AS 2-D ARRAY
np.savetxt(path + 'analysis_results.csv', results.reshape((n, 9)), fmt='%s',  
           delimiter=',')
print(bcolors.OKGREEN + 'Image analysis completed successfully.' + bcolors.ENDC)