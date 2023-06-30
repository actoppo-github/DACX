__author__ = 'Arnold C. Toppo'

from dataclasses import dataclass


@dataclass
class Washcoat:
    loading: float = 0.3766

    # equivalent to roughly 1.5 g/in^3
    def mass_ratio(self):
        return self.loading
