__author__ = 'Arnold C. Toppo'

import numpy as np
import scipy.integrate as integrate

pi = np.pi

def spiral_length(spiral_id, spiral_od, sheet_thickness, gap):
    distance = gap + sheet_thickness
    theta_init = pi * spiral_id / distance
    theta_fin = pi * spiral_od / distance

    length_func = lambda phi: distance * (0.5 / pi) * (1 + phi ** 2) ** 0.5
    length = integrate.quad(length_func, theta_init, theta_fin)[0]
    n_turns = (theta_fin - theta_init) / (2 * pi)

    outputs = length, n_turns
    print(outputs)

