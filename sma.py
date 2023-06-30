__author__ = 'Arnold C. Toppo'

from substrate import Monolith, MonolithDim, StackedSheets, FoldedSheets, SpiralSheets, Substrate
from washcoat import Washcoat
from typing import ClassVar
from material_properties import SubstrateMaterialProperties, WashcoatMaterialProperties
from dataclasses import dataclass, field


# washcoat ordinarily calculated as a function of GSA, pore size, pore size distribution, etc. and substrate properties
# temporarily placeholder is mass_ratio

@dataclass
class Washcoat:
    substrate: [ClassVar[float]]
    loading: float = 0.3766

    # equivalent to roughly 1.5 g/in^3
    def mass_ratio(self):
        return self.loading


@dataclass
class SMA:
    washcoat: Washcoat

    def washcoat_mass(self):
        return self.washcoat.substrate.mass() * self.washcoat.mass_ratio()

    def mass(self):
        return self.washcoat_mass() + self.washcoat.substrate.mass()

    def hydraulic_diam(self):
        return self.washcoat.substrate.geometry.channel_height


smp1 = SubstrateMaterialProperties(27.85, 2, 3, 1)
md1 = MonolithDim(monolith_width=6, monolith_height=6, channel_width=0.95 / 25.4,
                  channel_height=0.95 / 25.4, wall_thickness=3 / 1000)
monolith1 = Monolith(materialproperties=smp1, geometry=md1, monolith_length=8.56)

washcoat1 = Washcoat(monolith1, loading=0.3766)
sorbent = SMA(washcoat1)
print(sorbent.washcoat_mass(), sorbent.mass())
