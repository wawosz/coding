import numpy as np
import pyvista

# make a uniform 3d point field
x = np.linspace(0, 10, 10)      # 10 points uniformly spread
y = np.linspace(0, 1, 2)        # 2 points uniformly spread
z = np.linspace(0, 1, 2)        # 2 points uniformly spread

# create a mesh
xx, yy, zz = np.meshgrid(x, y, z)
centers = np.vstack((xx.ravel(), yy.ravel(), zz.ravel())).T

# make a bunch of spheres
spheres = [pyvista.Sphere(center=center) for center in centers]

# let's define array d which will contain count values
# for each point of the grid. Now array d is filled with random
# integer values
d = np.random.randint(low=1, high=100, size=842)

# plot it with smooth shading because we can
pyvista.plot(spheres, smooth_shading=True, scalars=d)