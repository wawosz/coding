#!/usr/bin/env python

# This simple example shows how to do basic rendering and pipeline
# creation.

import vtk
# The colors module defines various useful colors.
from vtk.util.colors import tomato

#----- DIFFERENT OBJECTS DEFINITIONS -----#

# This creates a polygonal cylinder model with circumferential facets
cylinderSource = vtk.vtkCylinderSource()
cylinderSource.SetResolution(100) # how many facets?

# Create a sphere
sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0.0, 0.0, 0.0)
sphereSource.SetRadius(5.0)
# Make the surface smooth.
sphereSource.SetPhiResolution(100)
sphereSource.SetThetaResolution(100)

# so, what object to visualize?
# objectSource = sphereSource
objectSource = cylinderSource

# The mapper is responsible for pushing the geometry into the graphics
# library. It may also do color mapping, if scalars or other
# attributes are defined.
objectMapper = vtk.vtkPolyDataMapper()
objectMapper.SetInputConnection(objectSource.GetOutputPort())

# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it -22.5 degrees.
objectActor = vtk.vtkActor()
objectActor.SetMapper(objectMapper)
objectActor.GetProperty().SetColor(tomato)
objectActor.RotateX(30.0)
objectActor.RotateY(-45.0)

# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renderer, set the background and size
ren.AddActor(objectActor)
ren.SetBackground(0, 0, 0)
renWin.SetSize(400, 400)

# This allows the interactor to initalize itself. It has to be
# called before an event loop.
iren.Initialize()

# We'll zoom in a little by accessing the camera and invoking a "Zoom"
# method on it.
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

# Start the event loop.
iren.Start()
