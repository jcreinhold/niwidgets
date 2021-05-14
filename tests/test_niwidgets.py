#!/usr/bin/env python

"""Tests for `niwidgets` package."""

from niwidgets import SurfaceWidget, NiftiWidget
from niwidgets.example_data import example_surface, example_t1


def test_surfacewidget():
    SurfaceWidget(example_surface)


def test_niftiwidget():
    NiftiWidget(example_t1)
