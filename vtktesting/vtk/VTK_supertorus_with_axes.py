# !/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk


def main():
    colors = vtk.vtkNamedColors()

    # colors.SetColor("BkgColor", [26, 51, 102, 255])

    # Definition of a supertorus and its parameters
    surface = vtk.vtkParametricSuperToroid()
    surface.SetN1(1.0)
    surface.SetN2(1.0)
    surface.SetXRadius(1.0)
    surface.SetYRadius(1.0)
    surface.SetZRadius(1.0)
    surface.SetRingRadius(1.0)
    surface.SetCrossSectionRadius(0.5)

    backProperty = vtk.vtkProperty()
    backProperty.SetColor(colors.GetColor3d("Tomato"))

    # Create a parametric function source
    source = vtk.vtkParametricFunctionSource()
    source.SetParametricFunction(surface)

    # Create a renderer
    renderer = vtk.vtkRenderer()

    # Create a mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    # assign actor's color as RGB value
    actor.GetProperty().SetColor(0, 0, 1.0)
    actor.GetProperty().SetOpacity(1.0)
    # visualize actor's edges
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetEdgeColor(0.2, 0.2, 0.2)
    # actor.SetBackfaceProperty(backProperty)
    # actor.GetProperty().SetDiffuseColor(colors.GetColor3d("Tomato"))
    # actor.GetProperty().SetSpecular(.5)
    # actor.GetProperty().SetSpecularPower(20)

    # Create a render window
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Parametric Objects Super Toroid Demo")
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(640, 480)

    # Add actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("Black"))
    
    # Add axes after the translation to the new coordinates
    transform = vtk.vtkTransform()
    transform.Translate(1.0, 0.0, 0.0)
    axes = vtk.vtkAxesActor()
    axes.SetUserTransform(transform)
    renderer.AddActor(axes)

    # Create an interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    # Setup a camera and final rendering
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(-30)
    renderer.GetActiveCamera().Zoom(0.9)
    renderer.ResetCameraClippingRange()
    renderWindow.Render()

    interactor.Initialize()
    interactor.Start()


if __name__ == '__main__':
    main()
