import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 1)
y = np.arange(-10, 10, 1)
z = np.arange(-10, 10, 1)
x, y, z = np.meshgrid(x, y, z)

grid = pv.StructuredGrid(x, y, z)
print(grid.points.shape)

# let's define array d which will contain count values
# for each point of the grid. Now array d is filled with random
# integer values
d = np.random.randint(low=1, high=100, size=grid.points.shape)

# or you can fill the scalar values with zeros
# d = np.zeros_like(grid.points)

grid.plot(show_edges=True, scalars=d[:, 1],
          stitle='Counts (CPM)')

# next example: opacity transfer function (opacity of each cell depends
# on the scalar value). Example from pyvista project page:
# https://docs.pyvista.org/examples/02-plot/opacity.html
opacity = [0, 0.2, 0.9, 0.6, 0.3]

# Have PyVista interpolate the transfer function
tf = pv.opacity_transfer_function(opacity, 100).astype(float) / 100.

plt.plot(tf)
plt.title('My Interpolated Opacity Transfer Function')
plt.ylabel('Opacity')
plt.xlabel('Index along scalar mapping')
plt.show()

grid.plot(show_edges=True, scalars=d[:, 1], opacity=opacity,
          stitle='Counts (CPM) with Opacity')