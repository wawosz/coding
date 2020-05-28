# !/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk


def main():
    colors = vtk.vtkNamedColors()

    colors.SetColor("BkgColor", [26, 51, 102, 255])

    surface = vtk.vtkParametricSuperToroid()
    source = vtk.vtkParametricFunctionSource()

    renderer = vtk.vtkRenderer()
    mapper = vtk.vtkPolyDataMapper()
    actor = vtk.vtkActor()

    backProperty = vtk.vtkProperty()
    backProperty.SetColor(colors.GetColor3d("Tomato"))

    # Create a parametric function source, renderer, mapper, and actor
    source.SetParametricFunction(surface)

    mapper.SetInputConnection(source.GetOutputPort())

    actor.SetMapper(mapper)

    # setting the actor's color
    # as named color
    # actor.GetProperty().SetColor(colors.GetColor3d("Red"))
    # as RGB value
    actor.GetProperty().SetColor(0, 0, 1.0)
    actor.GetProperty().SetOpacity(1.0)

    # visualize actor's edges
    actor.GetProperty().EdgeVisibilityOn()
    actor.GetProperty().SetEdgeColor(0.3, 0.3, 0.3)
    # actor.SetBackfaceProperty(backProperty)
    # actor.GetProperty().SetDiffuseColor(colors.GetColor3d("Tomato"))
    # actor.GetProperty().SetSpecular(.5)
    # actor.GetProperty().SetSpecularPower(20)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Parametric Objects Super Toroid Demo")
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(640, 480)
    renderer.AddActor(actor)
    # renderer.SetBackground(colors.GetColor3d("BkgColor"))
    renderer.SetBackground(colors.GetColor3d("Black"))

    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(-30)
    renderer.GetActiveCamera().Zoom(0.9)
    renderer.ResetCameraClippingRange()

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

# Supertorus parameters
    surface.SetN1(1.0)
    surface.SetN2(1.0)
    surface.SetXRadius(1.0)
    surface.SetYRadius(1.0)
    surface.SetZRadius(1.0)
    surface.SetRingRadius(1.0)
    surface.SetCrossSectionRadius(0.5)

# Final rendering
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
