import math
import numpy as np

from P_tank import P_tank



oxidizer_fuel_ratio = 3.21
propellant_mass = 34.87
l_d_ratio = 25.23
interval_check_precision = .34

ptank = P_tank()
tup = ptank.tank_length_diam(oxidizer_fuel_ratio,propellant_mass, l_d_ratio, interval_check_precision)
print(tup[0],tup[1])
