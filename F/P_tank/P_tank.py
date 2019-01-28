import math
import numpy as np

#Create a Rocket Class
class P_tank():

    lox_density = 1.140
    kero_density = 1.02


    def __init__(self):
        p = self

    def calculate_tank_volume(self, oxidizer_fuel_ratio, propellant_mass):
        kero_mass = propellant_mass/(1+oxidizer_fuel_ratio)
        lox_mass = propellant_mass - kero_mass

        kero_vol = kero_mass * self.kero_density
        lox_vol = lox_mass * self.lox_density

        return kero_vol + lox_vol


    def tank_length_diam_sub(self,volume,l_d_ratio, interval_check_precision):

        diameter = ((4*volume)/(math.pi*l_d_ratio))**(1. /3)
        length = l_d_ratio*diameter

        return diameter, length, l_d_ratio


    def tank_length_diam(self, oxidizer_fuel_ratio, propellant_mass,l_d_ratio, interval_check_precision):
        vol = self.calculate_tank_volume(oxidizer_fuel_ratio, propellant_mass)
        return self.tank_length_diam_sub(vol,l_d_ratio, interval_check_precision)
