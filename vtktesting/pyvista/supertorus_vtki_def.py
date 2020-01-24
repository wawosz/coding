#
# Script written in Python to plot supertoroidal surfaces
# using various parameters
#
# Wawrzyniec L. Dobrucki, Ph.D.
#

import pyvista
import numpy as np
import random
import matplotlib.pyplot as plt


def supertorus(yScale, xScale, Height, InternalRadius, Vertical, Horizontal,
               deltaX=0, deltaY=0, deltaZ=0):
  
    #  initial range for values used in parametric equation
    n = 100
    u = np.linspace(-np.pi, np.pi, n)
    t = np.linspace(-np.pi, np.pi, n)
    u, t = np.meshgrid(u, t)

    # a1: Y Scale <0, 2>
    a1 = yScale
    # a2: X Scale <0, 2>
    a2 = xScale
    # a3: Height <0, 5>
    a3 = Height
    # a4: Internal radius <0, 5>
    a4 = InternalRadius
    # e1: Vertical squareness <0.25, 1>
    e1 = Vertical
    # e2: Horizontal squareness <0.25, 1>
    e2 = Horizontal

    # Definition of parametric equation for supertorus
    x = a1 * (a4 + np.sign(np.cos(u)) * np.abs(np.cos(u)) ** e1) *\
        np.sign(np.cos(t)) * np.abs(np.cos(t)) ** e2
    y = a2 * (a4 + np.sign(np.cos(u)) * np.abs(np.cos(u)) ** e1) *\
        np.sign(np.sin(t)) * np.abs(np.sin(t)) ** e2
    z = a3 * np.sign(np.sin(u)) * np.abs(np.sin(u)) ** e1
    
    grid = pyvista.StructuredGrid(x + deltaX + 5, y + deltaY + 5, z + deltaZ)
    return grid 

# Create and plot structured grid
# To define supertori use the following function (defined above)
# supertorus(yScale, xScale, Height, InternalRadius, Vertical, Horizontal,
#            deltaX=0, deltaY=0, deltaZ=0)

# background image 100x100 pixels
image = pyvista.read('images/hindlimb.jpg')

# same image but rescaled to 10x10 pixels in grayscale
image10 = plt.imread('images/hindlimb10.jpg')
image10_gray = 0.2989 * image10[:,:,0] + 0.5870 * image10[:,:,1] + 0.1140 * image10[:,:,2] 

print('Plotting ...')

# setup the screen to plot image
p = pyvista.Plotter()
p.add_mesh(image, cmap='Greys_r')
p.show_bounds(grid='front', xlabel='', ylabel='', zlabel='', location='outer', all_edges=True)
p.remove_scalar_bar()
p.set_background(color='black')

# initialize indexes
i10 = -1
j10 = -1

# create supertori based on 10 x 10 background image
for i in range(0, 100, 10):
    i10 = i10 + 1
    j10 = -1
    for j in range(0, 100, 10):
        j10 = j10 + 1
        # perfusion = 5 * random.random()
        # image10_gray array needs to be transposed to match background image
        image10_point = image10_gray[9-j10, i10]/256
        perfusion = 0.1 + 5 * image10_point
        hypoxia = 4 * image10_point
        # squareness = 0.25 + random.random()
        squareness = 1
        surface = supertorus(yScale=1.25, xScale=1.25,
                             Height=perfusion,
                             InternalRadius=hypoxia,
                             Vertical=1,
                             Horizontal=squareness,
                             deltaX=i, deltaY=j, deltaZ=perfusion)
        p.add_mesh(surface, color=[image10_point * random.random(), 0.4, 1], opacity=1)


p.view_xy()
p.screenshot('images/glyph_image_xy.png')

p.view_isometric()
p.screenshot('images/glyph_image_isometric.png')

p.show()