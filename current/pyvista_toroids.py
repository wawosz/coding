#
# Script written in Python to plot supertoroidal surfaces
# using various parameters
#
# Wawrzyniec L. Dobrucki, Ph.D.
#

import pyvista
import numpy as np
#import random
#import matplotlib.pyplot as plt


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

print('Plotting ...')

# setup the plotter
p = pyvista.Plotter()
p.set_background(color='black')

# create supertori with different internal radius
dx = 0
dy = 0
for i in np.arange(1, 5, 1):
    dx += 10
    dz = 1
    mesh = supertorus(yScale = 1.0, xScale = 1.0,
                      Height=1.0,
                      InternalRadius=i,
                      Vertical=1,
                      Horizontal=1,
                      deltaX=dx, deltaY=dy, deltaZ=dz)
    p.add_mesh(mesh, color=[0.5, 0.5, 1], opacity=1)

# create supertori with different height
dx = 0
dy = 10
for i in np.arange(0, 4, 1):
    dx += 10
    dz = i
    mesh = supertorus(yScale = 1.0, xScale = 1.0,
                      Height=i,
                      InternalRadius=3,
                      Vertical=1,
                      Horizontal=1,
                      deltaX=dx, deltaY=dy, deltaZ=dz)
    p.add_mesh(mesh, color=[0.5, 0.5, 1], opacity=1)

# create supertori with different vertical squareness
dx = 0
dy = 20
for i in np.arange(0.2, 2, 0.5):
    dx += 10
    dz = 1
    mesh = supertorus(yScale = 1.0, xScale = 1.0,
                      Height=1.0,
                      InternalRadius=3,
                      Vertical=i,
                      Horizontal=1,
                      deltaX=dx, deltaY=dy, deltaZ=dz)
    p.add_mesh(mesh, color=[0.5, 0.5, 1], opacity=1)

# create supertori with different horizontal squareness
dx = 0
dy = 30
for i in np.arange(0.2, 2, 0.5):
    dx += 10
    dz = 1
    mesh = supertorus(yScale = 1.0, xScale = 1.0,
                      Height=1.0,
                      InternalRadius=3,
                      Vertical=1,
                      Horizontal=i,
                      deltaX=dx, deltaY=dy, deltaZ=dz)
    p.add_mesh(mesh, color=[0.5, 0.5, 1], opacity=1)

# create supertori with different color gradient
dx = 0
dy = 40
for i in np.arange(0.2, 1, 0.2):
    dx += 10
    dz = 1
    mesh = supertorus(yScale = 1.0, xScale = 1.0,
                      Height=1.0,
                      InternalRadius=3,
                      Vertical=1,
                      Horizontal=1,
                      deltaX=dx, deltaY=dy, deltaZ=dz)
    p.add_mesh(mesh, color=[i, 0, i], opacity=1)

# p.view_xy()
# p.show(screenshot='glyphs_xy.png')

p.view_isometric()
p.show(screenshot='glyphs_isometric.png')