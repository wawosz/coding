from vtk import *
t1=vtkParametricTorus() # An parametric representation of the torus
t2=vtkParametricTorus()
pfs=vtkParametricFunctionSource() # Generate a mesh from the parametric function
m=vtkPolyDataMapper() #The standard rendering pipeline
act=vtkActor()
ren=vtkRenderer()
win=vtkRenderWindow()
inter=vtkRenderWindowInteractor()
pfs.SetParametricFunction(t)
pfs.Update()
m.SetInputConnection(pfs.GetOutputPort())
act.SetMapper(m)
ren.AddActor(act)
win.AddRenderer(ren)
inter.SetRenderWindow(win)
win.Render()
inter.Start()