__author__ = 'Arnold C. Toppo'

import numpy as np
import scipy.integrate as integrate


class MonolithGeom:
    def __init__(self, monolith_width, monolith_height, monolith_length, channel_width, channel_height, wall_thickness):
        self.monolith_width = monolith_width
        self.monolith_height = monolith_height
        self.monolith_length = monolith_length
        self.channel_width = channel_width
        self.channel_height = channel_height
        self.wall_thickness = wall_thickness

    def total_area(self):
        total_area = self.monolith_width * self.monolith_height
        return total_area

    def void_area(self):
        # Calculate the number of channels in the monolith
        num_channels_horizontal = int(self.monolith_width / (self.channel_width + self.wall_thickness))
        num_channels_vertical = int(self.monolith_height / (self.channel_height + self.wall_thickness))
        total_channels = num_channels_horizontal * num_channels_vertical

        # Calculate the area of a single cell including the wall thickness
        cell_area = (self.channel_width + self.wall_thickness) * (self.channel_height + self.wall_thickness)

        # Calculate the total frontal solid area
        void_area = total_channels * cell_area

        return void_area

    def solid_area(self):
        solid_area = self.total_area() - self.void_area()
        return solid_area

    def void_volume(self):
        void_volume = self.void_area() * self.monolith_length
        return void_volume

    def solid_volume(self):
        solid_volume = self.solid_area() * self.monolith_length
        return solid_volume


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

# class SpiralCorrugationGeom:
#     def __init__(self, sheet_width, sheet_thickness, sheet_gap):
#         self.sheet_width = sheet_width
#         self.sheet_thickness = sheet_thickness


class StackedSheetsGeom:
    def __init__(self, sheet_width, sheet_length, sheet_thickness, sheet_gap, stack_height):
        self.geometry = 'Stacked Sheets'
        self.sheet_width = sheet_width
        self.sheet_length = sheet_length
        self.sheet_thickness = sheet_thickness
        self.sheet_gap = sheet_gap
        self.stack_height = stack_height

    def n_sheets(self):
        n_sheets = int(self.stack_height / (self.sheet_thickness + (self.sheet_thickness + self.sheet_gap)))
        return n_sheets

    def material_length(self):
        material_length = self.n_sheets() * self.sheet_length
        return material_length

    def material_volume(self):
        material_volume = self.sheet_thickness * self.sheet_width * self.material_length()
        return material_volume


class FoldedSheetsGeom:
    def __init__(self, sheet_width, sheet_length, sheet_thickness, sheet_gap, stack_height):
        self.geometry = 'Folded Sheets'
        self.sheet_width = sheet_width
        self.sheet_length = sheet_length
        self.sheet_thickness = sheet_thickness
        self.sheet_gap = sheet_gap
        self.stack_height = stack_height

    def n_sheets(self):
        n_sheets = int(self.stack_height / (self.sheet_thickness + (self.sheet_thickness + self.sheet_gap)))
        return n_sheets

    def material_length(self):
        material_length = self.n_sheets() * self.sheet_length + (self.n_sheets() - 1) * self.sheet_gap * np.pi / 2
        return material_length

    def material_volume(self):
        material_volume = self.sheet_thickness * self.sheet_width * self.material_length()
        return material_volume


print('geometryproperties')
