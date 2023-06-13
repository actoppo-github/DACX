__author__ = 'Arnold C. Toppo'

import math


class AdsorptionEnergy:
    def __init__(self, whsv, fan_diam):
        self.whsv = whsv
        self.fan_diam = fan_diam

    # def e_fan:
    #     return


class RegenerationEnergy:
    def __init__(self, mass_adsorbent, cp_adsorbent, mass_co2, t_init, t_fin, p_out, p1, p2):
        self.mass_adsorbent = mass_adsorbent
        self.cp_adsorbent = cp_adsorbent
        self.mass_co2 = mass_co2
        self.t_init = t_init
        self.t_fin = t_fin
        self.p_out = p_out
        self.p1 = p1
        self.p2 = p2

    def cp_co2(self, T):
        T = T/1000
        cpa_co2 = 24.99735
        cpb_co2 = 55.18696
        cpc_co2 = -33.69137
        cpd_co2 = 7.948387
        cpe_co2 = -0.136638
        cp_co2 = cpa_co2 + cpb_co2 * T + cpc_co2 * T ** 2 + cpd_co2 * T ** 3 + cpe_co2 * T ** (-2)
        return cp_co2

    def es_adsorbent(self):
        return self.mass_adsorbent * self.cp_adsorbent * (self.t_fin - self.t_init)

    def es_co2(self):
        return self.mass_co2 * self.cp_co2() * (self.t_fin - self.t_init)

    def edes_co2(self):
        return 5

    def evac(self, V):
        evac = self.p_out * V * ((self.p1 / self.p_out) - (self.p2 / self.p_out) + math.log(self.p2 / self.p1))
        return evac

    def eregen_tot(self):
        return self.es_adsorbent() + self.es_co2() + self.edes_co2() + self.evac()
