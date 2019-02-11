import math
import numpy as np

from P_tank import P_tank



oxidizer_fuel_ratio = 3.21
propellant_mass = 161 #kg
l_d_ratio = 25.23


ptank = P_tank()
tup = ptank.tank_length_diam(oxidizer_fuel_ratio,propellant_mass, l_d_ratio)
print(tup[0],tup[1])
