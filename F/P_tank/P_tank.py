import math
import numpy as np

#Create a Rocket Class
class P_tank():
    '''
    Determine tank length from type, diameter, mass, and ulage.

    Parameters
    ----------
    type : string
        Tank type (either propellant or lox)
    diameter : numeric
        Diameter of the rocket body cross section
    x_mass : numeric
        Total mass of propellant / lox within tank
    ulage : numeric
        Total mass of ulage within tank

    Returns
    -------
    tank_length_diam : numeric
        Length of tank

    Notes
    -----
    The following assumptions are made

    ==========================  ============================
    Parameter                   Value
    ==========================  ============================
    Density of RP-1             804.59 kg/m^3 @ 1 atm   [1]
    Density of Liquid Oxygen    1141 kg/m^3 @ 293 K     [2]
    ==========================  ============================

    Created by Buddha and Max for Loyola MARS Base11 1-30-2019

    References
    ----------
    [1]
    [2] https://ws680.nist.gov/publication/get_pdf.cfm?pub_id=832303
    '''

    def __init__(self):
        self.lox_density = 1141     #kg/m**3 [1]
        self.kero_density = 804.59   #kg/m**3 [2]

    def calculate_tank_volume(self, oxidizer_fuel_ratio, propellant_mass):
        kero_mass = propellant_mass/(1 + oxidizer_fuel_ratio)
        lox_mass = propellant_mass - kero_mass

        kero_vol = kero_mass * self.kero_density
        lox_vol = lox_mass * self.lox_density

        return kero_vol + lox_vol


    def tank_length_diam_sub(self,volume,l_d_ratio):

        diameter = ((4*volume)/(math.pi*l_d_ratio))**(1. /3)
        length = l_d_ratio*diameter

        return diameter, length, l_d_ratio


    def tank_length_diam(self, oxidizer_fuel_ratio, propellant_mass,l_d_ratio):
        vol = self.calculate_tank_volume(oxidizer_fuel_ratio, propellant_mass)
        return self.tank_length_diam_sub(vol,l_d_ratio)
