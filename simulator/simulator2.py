#
#  _ _ _ _____ _ _ _ _____ _____ _____
# | | | |  _  | | | |     |   __|__   |
# | | | |     | | | |  |  |__   |   __|
# |_____|__|__|_____|_____|_____|_____|
#
# (C) 2019 by Wawrzyniec L. Dobrucki
# wawosz@gmail.com
#
# Syntax: python simulator.py
#

# import standard modules
import matplotlib.pyplot as plt
import numpy as np
import random


# Definition of Voxel class. Each pixel (voxel) on the image is a class. 
# Class contains several parameters and methods.
#
# Parameters:
# .half_life: half-life for given isotope (i.e. minutes)
# .decay_constant = ln(2) / half_life
# .initial_activity: initial activity in the voxel
#
# Methods:
# .decay(initial_activity, decay_constant, time): outputs decayed_activity(t)
#      .decayed_activity(t) = initial_activity * e^(-decay_constant * time)
#

class Voxel:
    # definition and initialization of class parameters
    def __init__(self):
        self.half_life = 0              # initialize half-life value
        self.decay_constant = 0         # decay constant calculated as ln(2)/HL
        self.initial_activity = 0       # initial activity in the voxel
        self.decayed_activity = 0       # activity after some time (decayed)
    # definition of class methods
    # method "decay" to calculate activity of a pixel after time t
    def decay(self, initial_activity, decay_constant, time):
        decayed_activity = initial_activity * np.exp(-decay_constant * time)
        return decayed_activity

# create a list of classes Voxel (for image 20x20 = 400 voxels)
voxel_list = [Voxel() for i in range(400)]

# populate classes with initial values (random)
for vox in voxel_list:
    vox.initial_activity = random.random()

# create a grid 20x20 for plotting voxels at time 0
grid_0 = []
for x in range(0, 400):
    grid_0.append(voxel_list[x].initial_activity)
grid_0 = np.array(grid_0).reshape(20, 20)   # reshape array of 400 values into 20x20

# create a grid 20x20 for plotting voxels after some time (here time=10)
grid_t = []
for x in range(0, 400):
    voxel_list[x].decayed_activity = \
        voxel_list[x].decay(voxel_list[x].initial_activity, 0.115524, 10)
    grid_t.append(voxel_list[x].decayed_activity)
grid_t = np.array(grid_t).reshape(20, 20)   # reshape array of 400 values into 20x20

# plot two graphs side-by-side
fig, (ax1, ax2) = plt.subplots(ncols=2)
im1 = ax1.imshow(grid_0, interpolation='None', cmap='binary', vmin=0, vmax=1)
ax1.set_title('Plot at time 0')
im2 = ax2.imshow(grid_t, interpolation='None', cmap='binary', vmin=0, vmax=1)
ax2.set_title('Plot at time t')
fig.subplots_adjust(wspace=0.4)
fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
plt.show()
