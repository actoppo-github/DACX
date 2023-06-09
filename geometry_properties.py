__author__ = 'Arnold C. Toppo'

import numpy as np
import scipy.integrate as integrate
import math


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

    def material_length(self):
        def length_func(phi):
            return self.distance * (0.5 / np.pi) * (1 + phi ** 2) ** 0.5

        length = integrate.quad(length_func, self.theta_init, self.theta_fin)[0]
        return length

    def material_volume(self):
        material_volume = self.sheet_thickness * self.material_length() * self.sheet_width
        return material_volume

    def spiral_turns(self):
        n_turns = (self.theta_fin - self.theta_init) / (2 * np.pi)
        return n_turns


# just throw an error message if the enclosure dimensions are smaller than the spiral od

class SpiralCorrugationGeom:
    def __init__(self, sheet_width, sheet_thickness, sheet_gap):
        self.sheet_width = sheet_width
        self.sheet_thickness = sheet_thickness


class StackedSheetsGeom:
    def __init__(self, sheet_width, sheet_length, sheet_thickness, sheet_gap, stack_height):
        self.geometry = 'Stacked Sheets'
        self.sheet_width = sheet_width
        self.sheet_length = sheet_length
        self.sheet_thickness = sheet_thickness
        self.sheet_gap = sheet_gap
        self.stack_height = stack_height

    def n_sheets(self):
        n_sheets = math.floor(self.stack_height / (self.sheet_thickness + (self.sheet_thickness + self.sheet_gap)))
        return n_sheets

    def material_length(self):
        material_length = self.n_sheets() * self.sheet_length
        return material_length

    def material_volume(self):
        material_volume = self.sheet_thickness * self.sheet_width * self.material_length()
        return material_volume

class FoldedSheetsGeom:
    def __init__(self, sheet_width, sheet_length, sheet_thickness, sheet_gap, stack_height):
        self.geometry = 'Stacked Sheets'
        self.sheet_width = sheet_width
        self.sheet_length = sheet_length
        self.sheet_thickness = sheet_thickness
        self.sheet_gap = sheet_gap
        self.stack_height = stack_height

    def n_sheets(self):
        n_sheets = math.floor(self.stack_height / (self.sheet_thickness + (self.sheet_thickness + self.sheet_gap)))
        return n_sheets

    def material_length(self):
        material_length = self.n_sheets() * self.sheet_length + (self.n_sheets()-1)*
        return material_length

    def material_volume(self):
        material_volume = self.sheet_thickness * self.sheet_width * self.material_length()
        return material_volume

print('geometryproperties')
