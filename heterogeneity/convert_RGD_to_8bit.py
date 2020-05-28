# converting RGB TIF files from chosen folder to 8-bit
import os
import glob
import numpy as np
import tkinter as tk
from PIL import Image
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

# list specific files
n = 1
for filename in glob.glob(os.path.join(path, '*.tif')):
    print(str(n), filename)
    n = n + 1
    img = Image.open(filename).convert('L')
    img.save(filename + '_converted.tif')

# print in green color selected path
print(bcolors.OKGREEN + 'Conversion to grayscale 8-bit completed' + bcolors.ENDC)