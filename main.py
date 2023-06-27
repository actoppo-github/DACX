__author__ = 'Arnold C. Toppo'

from geometry_properties import Monolith, MonolithDim, StackedSheets, FoldedSheets, SpiralSheets
from material_properties import SubstrateMaterialProperties, SorbentMaterialProperties


smp1 = SubstrateMaterialProperties(27.85, 2, 3, 1)
md1 = MonolithDim(monolith_width=6, monolith_height=6, channel_width=0.95/25.4,
                  channel_height=0.95/25.4, wall_thickness=3/1000)
c = Monolith(materialproperties=smp1, geometry=md1, monolith_length=8.56)
print(c.geometry.total_channels())
print(c.geometry.void_area())
print(c.solid_volume())
print(c.geometry.csarea())
print(c.mass())
print(c.geometry.total_channels()/c.geometry.total_area())
