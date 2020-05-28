#
# Script written in Python to plot supertoroidal surfaces
# using various parameters
#
# Wawrzyniec L. Dobrucki, Ph.D.
#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import random


def supertorus(yScale, xScale, Height, InternalRadius, Vertical, Horizontal,
               Color, deltaX=0, deltaY=0, deltaZ=0):
    # range for values used in parametric equation
    n = 300
    u = np.linspace(-np.pi, np.pi, n)
    t = np.linspace(-np.pi, np.pi, n)
    u, t = np.meshgrid(u, t)

    # a1: Y Scale <0, 5>
    a1 = yScale
    # a2: X Scale <0, 5>
    a2 = xScale
    # a3: Height <0, 5>
    a3 = Height
    # a4: Internal radius <0, 5>
    a4 = InternalRadius
    # e1: Vertical squareness <0.25, 1>
    e1 = Vertical
    # e2: Horizontal squareness <0.25, 1>
    e2 = Horizontal
    # c1: Color
    c1 = Color
    # Definition of parametric equation for supertorus
    x = a1 * (a4 + np.sign(np.cos(u)) * abs(np.cos(u)) ** e1) *\
        np.sign(np.cos(t)) * abs(np.cos(t)) ** e2
    y = a2 * (a4 + np.sign(np.cos(u)) * abs(np.cos(u)) ** e1) *\
        np.sign(np.sin(t)) * abs(np.sin(t)) ** e2
    z = a3 * np.sign(np.sin(u)) * abs(np.sin(u)) ** e1
    surf = ax.plot_surface(x + deltaX, y + deltaY, z + deltaZ,
                           rstride=10, cstride=10, linewidth=0.1,
                           color=c1, edgecolors='k')
    return surf


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_zlim(0, 20)

for i in range(0, 20, 10):
    for j in range(0, 20, 10):
        perfusion = 1 + random.random()
        hypoxia = 2
        squareness = 0.25 + random.random()
        surface = supertorus(yScale=1, xScale=1,
                             Height=perfusion,
                             InternalRadius=hypoxia,
                             Vertical=1,
                             Horizontal=squareness,
                             Color='gray',
                             deltaX=i, deltaY=j, deltaZ=0)


ax.view_init(50, 0)
ax.set_axis_off()

# fig.colorbar(surface, shrink=0.5, aspect=5)
# this is the best format for high resolution publication-ready images
plt.savefig('supertori.eps', format='eps', dpi=300)
plt.show()
