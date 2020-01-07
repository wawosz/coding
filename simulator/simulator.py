import matplotlib.pyplot as plt
import numpy as np
import random


# Definition of Voxel class. Class will contain several parameters and methods
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
    def __init__(self):
        self.half_life = 0              # half-life value
        self.decay_constant = 0         # decay constant calculated as ln(2)/half_life
        self.initial_activity = 0       # initial activity in the voxel
        self.decayed_activity = 0       # activity after some time (decayed)

    def decay(self, initial_activity, decay_constant, time):
        decayed_activity = initial_activity * np.exp(-decay_constant * time)
        return decayed_activity

# dictionary (list) of selected isotopes and corresponding half-lifes
isotopes = {
    "tc99m":6.0,
    "tl201":73.1,
    "f18":2.0,
    "c11":0.33
}

# create a list of classes Voxel
voxel_list = [Voxel() for i in range(100)]

# populate classes with initial values
for vox in voxel_list:
    vox.initial_activity = random.random()

# this is how you can access single class element or plot a range of decayed values
# voxel_list[0].initial_activity = 100
# print(voxel_list[0].initial_activity)
# for t in range(0, 24):
#     test = voxel_list[0].decay(voxel_list[0].initial_activity, 0.115524, t)
#     plt.scatter(t, test)
#     print(test)
# plt.show()

# create a grid 10x10 for plotting voxels at time 0
grid_0 = []
for x in range(0, 100):
    grid_0.append(voxel_list[x].initial_activity)
grid_0 = np.array(grid_0).reshape(10,10)

# create a grid 10x10 for plotting voxels after some time
grid_t = []
for x in range(0, 100):
    voxel_list[x].decayed_activity = voxel_list[x].decay(voxel_list[x].initial_activity, 0.115524, 10)
    grid_t.append(voxel_list[x].decayed_activity)
grid_t = np.array(grid_t).reshape(10,10)

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