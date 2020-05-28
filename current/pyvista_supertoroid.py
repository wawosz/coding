# PARAMETRIC SUPER TOROID IMPLEMENTATION IN PYVISTA
#
# pyvista.ParametricSuperToroid(ringradius=None, crosssectionradius=None, 
# xradius=None, yradius=None, zradius=None, n1=None, n2=None, **kwargs)
#
# ringradius (double, optional) – The radius from the center to the middle of 
#    the ring of the supertoroid. Default is 1.
# crosssectionradius (double, optional) – The radius of the cross section of
#    ring of the supertoroid. Default = 0.5.
# xradius (double, optional) – The scaling factor for the x-axis. Default is 1.
# yradius (double, optional) – The scaling factor for the y-axis. Default is 1.
# zradius (double, optional) – The scaling factor for the z-axis. Default is 1.
# n1 (double, optional) – The shape of the torus ring. Default is 1.
# n2 (double, optional) – The shape of the cross section of the ring. 
#    Default is 1.

import pyvista as pv

# create supertorus #1
supertoroid = pv.ParametricSuperToroid(ringradius=1, crosssectionradius=0.5,
                                       xradius=1, yradius=1, zradius=3,
                                       n1=1, n2=1)

# create supertorus #2 and translate it to another position
# Note: to keep the heights OK, crosssectionradius*zradius should be the same
supertoroid2 = pv.ParametricSuperToroid(ringradius=1, crosssectionradius=0.1,
                                       xradius=1, yradius=1, zradius=15,
                                       n1=1, n2=1)
supertoroid2.translate([0, 0, 3])

# create plotting objects
plotter = pv.Plotter()
plotter.add_mesh(supertoroid, 'r')
plotter.add_mesh(supertoroid2, 'b')

# show plotted objects
plotter.show()

# alternatively, individual objects can be plotted as this:
# supertoroid.plot(color="tan", smooth_shading=True)
# supertoroid2.plot(color="red", smooth_shading=True)
