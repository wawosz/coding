import numpy as np
import pyvista as pv

# get dataset for the glyphs: supertoroid in xy plane
saucer = pv.ParametricSuperToroid(ringradius=1, n2=1, zradius=1)
saucer.rotate_y(90)
# saucer.plot()  #  <-- check how a single saucer looks like

# get dataset where to put glyphs
x,y,z = np.mgrid[-10:10, -10:10, :1]
mesh = pv.StructuredGrid(x, y, z)

# construct the glyphs on top of the mesh
glyphs = mesh.glyph(geom=saucer, factor=0.3)
# glyphs.plot()  #  <-- simplest way to plot it

# create Plotter and add our glyphs with some nontrivial lighting
plotter = pv.Plotter(window_size=(1000, 800))
plotter.add_mesh(glyphs, color=[0.5, 0.2, 0.2], specular=1, specular_power=15)

plotter.show()