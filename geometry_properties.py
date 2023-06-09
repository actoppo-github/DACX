__author__ = 'Arnold C. Toppo'

import numpy as np
import scipy.integrate as integrate


class SpiralSheetGeom:
    def __init__(self, inner_diam, outer_diam, sheet_width, sheet_thickness, sheet_gap):
        self.inner_diam = inner_diam
        self.outer_diam = outer_diam
        self.sheet_width = sheet_width
        self.sheet_thickness = sheet_thickness
        self.sheet_gap = sheet_gap
        self.distance = self.sheet_gap + self.sheet_thickness
        self.theta_init = np.pi * self.inner_diam / self.distance
        self.theta_fin = np.pi * self.outer_diam / self.distance

    def spiral_length(self):
        def length_func(phi):
            return self.distance * (0.5 / np.pi) * (1 + phi ** 2) ** 0.5

        self.length = integrate.quad(length_func, self.theta_init, self.theta_fin)[0]
        return self.length

    def spiral_volume(self):
        self.spiral_volume = self.sheet_thickness * self.spiral_length() * self.sheet_width
        return self.spiral_volume

    def spiral_turns(self):
        n_turns = (self.theta_fin - self.theta_init) / (2 * np.pi)
        return n_turns


class SpiralCorrugationGeom:
    def __init__(self, sheet_width, sheet_thickness, sheet_gap):
        self.sheet_width = sheet_width
        self.sheet_thickness = sheet_thickness


class StackedSheetsGeom:
    def __init__(self, sheet_width, sheet_length, sheet_height, sheet_thickness, sheet_gap):
        self.sheet_width = sheet_width
        self.sheet_length = sheet_length
        self.sheet_height = sheet_height
        self.sheet_thickness = sheet_thickness
        self.sheet_gap = sheet_gap


print('geometryproperties')
