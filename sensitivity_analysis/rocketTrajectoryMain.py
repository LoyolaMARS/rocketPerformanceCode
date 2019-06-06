''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * File name  :  RocketTrajectoryMain.py
 * Purpose    :  To rapidly test rocket trajectories for fufillment of mission design requirements
 * @author    :  Harrison Leece
 * @author    :  Debugged by
 * Date       :  2019-01-23
 * Notes      :  None
 * Warnings   :  None
 *
 *  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * Revision History
 * ================
 *   Ver      Date     Modified by:  Reason for change or modification
 *  -----  ----------  ------------  ---------------------------------------------------------------------
 *  1.0.0  2019-01-23  Harrison L    Initial release
 *  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

from Rocket import Rocket
from array import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


rocket = Rocket(2700, 730, .59, 230, 11.5/12, .25)
tuple = rocket.flight_simulation()

print("Max displacement: " + str(tuple[5]))
print("Burnout Time: " + str(tuple[4]))
print("Burnout Velocity: " +str(tuple[3]))
print("Burnout Altitude: " + str(tuple[6]))
print("Burnout mass: " + str(tuple[7]))
print("Mission Time: " + str(tuple[8]))
print("Burnout Acceleration: " + str(tuple[9]))
print("Mass flow rate: " + str(tuple[10]))
#Displacement subplot
plt.subplot(2, 1, 1)
plt.plot(tuple[2], tuple[0])
plt.title('Displacement vs time')
plt.ylabel('Displacement in feet')
#velocity subplot
plt.subplot(2, 1, 2)
plt.title('Velocity vs Time')
plt.ylabel('Upwards velocity in feet/s')
plt.xlabel('Time in seconds')
plt.plot(tuple[2], tuple[1])

plt.show()

thrust_range = np.linspace(2300, 3300, num=5)
displacement_vector1 = np.zeros(np.size(thrust_range))

for i in range(0,np.size(thrust_range)):
    thrust = thrust_range[i]
    rocket = Rocket(thrust, 730, .59, 230, 11.5/12, .25)
    tuple = rocket.flight_simulation()
    displacement_vector1[i] = tuple[5]
    print("thrust check: " + str(i))

mass_fraction_range = np.linspace(50, 70, num=5)
displacement_vector2 = np.zeros(np.size(mass_fraction_range))

for i in range(0,np.size(mass_fraction_range)):
    mf =  mass_fraction_range[i]
    rocket = Rocket(2700, 730, mf/100, 230, 11.5/12, .25)
    tuple2 = rocket.flight_simulation()
    displacement_vector2[i] = tuple2[5]
    print("mass_frac check: " + str(i))

mass_range = np.linspace(600, 800, num=5)
displacement_vector3 = np.zeros(np.size(mass_range))

for i in range(0,np.size(mass_range)):
    mass = mass_range[i]
    rocket = Rocket(2700, mass, .59, 230, 11.5/12, .25)
    tuple3 = rocket.flight_simulation()
    displacement_vector3[i] = tuple3[5]
    print("mass check: " + str(i))

dia_range = np.linspace(10, 13, num=4)
displacement_vector4 = np.zeros(np.size(dia_range))

for i in range(0, np.size(dia_range)):
    dia = dia_range[i]
    rocket = Rocket(2700, 730, .59, 230, dia/12, .25)
    tuple4 = rocket.flight_simulation()
    displacement_vector4[i] = tuple4[5]
    print("dia check: " + str(i))

plt.subplot(4,1,1)
plt.plot(thrust_range, displacement_vector1)
plt.title('Displacement vs thrust (lbf)')
plt.ylabel('Displacement in feet')
plt.subplot(4,1,2)
plt.plot(mass_fraction_range, displacement_vector2)
plt.title('Displacement vs mass fraction (%)')
plt.ylabel('Displacement in feet')
plt.subplot(4,1,3)
plt.plot(mass_range, displacement_vector3)
plt.title('Displacement vs liftoff mass (lbf)')
plt.ylabel('Displacement in feet')
plt.subplot(4,1,4)
plt.plot(dia_range, displacement_vector4)
plt.title('Displacement vs diameter (inch)')
plt.ylabel('Displacement in feet')
plt.show()


plt.show()
