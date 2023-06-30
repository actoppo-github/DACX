__author__ = 'Arnold C. Toppo'

from dataclasses import dataclass

@dataclass
class SubstrateMaterialProperties:
    density: float = 0
    voidage: float = 0
    thermal_conductivity: float = 0
    resistivity: float = 0

@dataclass
class WashcoatMaterialProperties:
    density: float = 0
    voidage: float = 0
    thermal_conductivity: float = 0
    resistivity: float = 0