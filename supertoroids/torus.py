#
# Sample python script to plot a torus using matplotlib
#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

n = 300

theta = np.linspace(0, 2. * np.pi, n)
phi = np.linspace(0, 2. * np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 4, 2
x = (c + a * np.cos(theta)) * np.cos(phi)
y = (c + a * np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim(-3, 3)
# below line is to plot a torus using color scale
#surf = ax.plot_surface(x, y, z, rstride=10, cstride=10, linewidth=0.1,
#                       cmap='Reds', color='k', edgecolors='k')

# if color is used in plot_surface then colorbar needs to be commented
#fig.colorbar(surf, shrink=0.5, aspect=5)

surf = ax.plot_surface(x, y, z, rstride=10, cstride=10, linewidth=0.1,
                       color=(0.1, 0.2, 0.5), edgecolors='w')

ax.view_init(30, 0)
ax.set_axis_off()

plt.show()
