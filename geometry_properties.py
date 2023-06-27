__author__ = 'Arnold C. Toppo'

from abc import ABC, abstractmethod
from material_properties import SubstrateMaterialProperties, SorbentMaterialProperties
# from energy import
from numpy import pi
from dataclasses import dataclass
import scipy.integrate as integrate


@dataclass
class GeneralGeometry(ABC):
    # this is a base class since all geometries have a length/depth, cross-sectional area, and volume. Care: not all
    # geometries have a volume which is the cross-sectional area multiplied by length/depth.
    # @abstractmethod
    def material_length(self):
        print("Material length is missing.")

    # @abstractmethod
    def csarea(self):
        print("Cross-Sectional Area is missing.")

    def volume(self):
        return self.material_length() * self.csarea()


@dataclass
class Substrate(ABC):
    # The substrate class "HAS A" material properties and geometry.
    materialproperties: SubstrateMaterialProperties
    geometry: GeneralGeometry


@dataclass
class MonolithDim(GeneralGeometry):
    monolith_width: float
    monolith_height: float
    channel_width: float
    channel_height: float
    wall_thickness: float

    def total_area(self):
        total_area = self.monolith_width * self.monolith_height
        return total_area

    def total_channels(self):
        # Calculate the number of channels in the monolith
        num_channels_horizontal = int(self.monolith_width / (self.channel_width + self.wall_thickness))
        num_channels_vertical = int(self.monolith_height / (self.channel_height + self.wall_thickness))
        total_channels = num_channels_horizontal * num_channels_vertical

        return total_channels

    def void_area(self):

        # Calculate the area of a single cell including the wall thickness
        cell_area = self.channel_width * self.channel_height
        # Calculate the total frontal solid area
        void_area = self.total_channels() * cell_area

        return void_area

    def csarea(self):
        solid_area = self.total_area() - self.void_area()
        return solid_area


@dataclass
class Monolith(Substrate):
    geometry: MonolithDim
    monolith_length: float

    def void_volume(self):
        void_volume = self.geometry.void_area() * self.monolith_length
        return void_volume

    def solid_volume(self):
        solid_volume = self.geometry.csarea() * self.monolith_length
        return solid_volume

    def mass(self) -> float:
        return self.solid_volume() * self.materialproperties.density


@dataclass
class SheetDim(GeneralGeometry):
    sheet_width: float
    sheet_thickness: float

    def csarea(self) -> float:
        return self.sheet_thickness * self.sheet_width


@dataclass
class SheetSubstrate(Substrate):
    geometry: SheetDim
    sheet_gap: float

    def material_length(self):
        print("Material length is missing.")

    # def print_geometry(self):
    #     print(self.geometry.sheet_width)
    #     print(self.geometry.volume())


@dataclass
class StackedSheets(SheetSubstrate):
    sheet_length: float
    stack_height: float

    def n_sheets(self) -> float:
        n_sheets = int(
            self.stack_height / (self.geometry.sheet_thickness + (self.geometry.sheet_thickness + self.sheet_gap)))
        return n_sheets

    def material_length(self) -> float:
        return self.n_sheets() * self.sheet_length

    def mass(self) -> float:
        return self.material_length() * self.materialproperties.density


@dataclass
class SpiralSheets(SheetSubstrate):
    inner_diam: float
    outer_diam: float

    def angles(self):
        distance = self.sheet_gap + self.geometry.sheet_thickness
        theta_init = pi * self.inner_diam / distance
        theta_fin = pi * self.outer_diam / distance
        return theta_init, theta_fin

    def material_length(self):
        theta_init, theta_fin = self.angles()

        def length_func(phi):
            return self.angles()[0] * (0.5 / pi) * (1 + phi ** 2) ** 0.5

        length = integrate.quad(length_func, theta_init, theta_fin)[0]
        return length

    def spiral_turns(self):
        theta_init, theta_fin = self.angles()
        n_turns = (theta_init - theta_fin) / (2 * pi)
        return n_turns

    def mass(self) -> float:
        return self.material_length() * self.materialproperties.density


@dataclass
class FoldedSheets(SheetSubstrate):
    def n_sheets(self) -> float:
        n_sheets = int(
            self.stack_height / (self.geometry.sheet_thickness + (self.geometry.sheet_thickness + self.sheet_gap)))
        return n_sheets

    def material_length(self) -> float:
        return self.n_sheets() * self.sheet_length

    def mass(self) -> float:
        return self.material_length() * self.materialproperties.density


# smp1 = SubstrateMaterialProperties(2.4, 2, 3, 1)
# sg1 = SheetDim(sheet_width=6, sheet_thickness=0.0787)
# md1 = MonolithDim(monolith_width=6, monolith_height=6, channel_width=0.05, channel_height=0.05, wall_thickness=0.007)
# a = StackedSheets(smp1, sg1, .1, .3, 10)
# b = SpiralSheets(materialproperties=smp1, geometry=sg1, sheet_gap=0, inner_diam=1, outer_diam=5)
# c = Monolith(materialproperties=smp1, geometry=md1, monolith_length=6)
#
#
# print(a.mass())
# print(a.material_length())
# print(b.mass())
# print(b.material_length())
# print(c.mass())
