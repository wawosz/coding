import numpy as np
import pyvista as pv
from pyvista import examples

mesh = examples.load_hexbeam()
print(mesh)
bcpos = [(6.20, 3.00, 7.50),
         (0.16, 0.13, 2.65),
         (-0.28, 0.94, -0.21)]

p = pv.Plotter()
p.add_mesh(mesh, show_edges=True, color='red')
# p.add_mesh(pv.PolyData(mesh.points), color='red',
#       point_size=10, render_points_as_spheres=True)
p.camera_position = [(6.20, 3.00, 7.50),
                 (0.16, 0.13, 2.65),
                 (-0.28, 0.94, -0.21)]
p.show(screenshot='beam_nodes.png')