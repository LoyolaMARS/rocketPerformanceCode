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


thrust_range = list(range(2000,3000,100))
weight_range = list(range(450,600,50))


##x_twoD_res = []
##for thrust in thrust_range:
##    oneD_res = []
##    for weight in weight_range:
##        rocket = Rocket(thrust, weight, .65, 230, 12/12, .25)
##        tuple = rocket.flight_simulation()
##        print(tuple[5])
##        oneD_res.append(tuple[5])
##    x_twoD_res.append(oneD_res)


##x_twoD_res = np.asarray(x_twoD_res)
##X,Y = np.meshgrid(thrust_range,weight_range)
##Z = x_twoD_res.reshape(X.shape)

##ax = plt.axes(projection='3d')
##ax.plot_surface(X,Y,Z)
##plt.show()


rocket = Rocket(2500, 530, .65, 230, 12/12, .25)
tuple = rocket.flight_simulation()


print("Max displacement: " + str(tuple[5]) + " feet")
print("Burnout Time: " + str(tuple[4]) + " seconds")
print("Burnout Velocity: " +str(tuple[3]) + " ft/s")
print("Burnout Altitude: " + str(tuple[6]) + " feet")
print("Burnout mass: " + str(tuple[7]) + " slugs")
print("Apogee Time: " + str(tuple[8]) + " seconds")
print("Burnout Acceleration: " + str(tuple[9]) + " ft/s^2")
print("Mass flow rate: " + str(tuple[10]) + " slug/s")
print("Max Q: " + str(tuple[11]) + " lbs/ft^2 or " + str((tuple[11] * 1/144)) + " psi" )
print("Displacement at Max Q: " + str(tuple[13]) + " feet")
print("Max Q time: " + str(tuple[15]) + " seconds")
print("Velocity at Max Q: " + str(tuple[12]) + " ft/s")
print("Acceleration at Max Q: " + str(tuple[14]) + " ft/s^2 or " +str(tuple[14]/32.174) + " Gs")
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
