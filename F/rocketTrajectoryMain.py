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


thrust_range = list(range(2000,4000,50))
weight_range = list(range(300,500,50))


x_twoD_res = []
for thrust in thrust_range:
    oneD_res = []
    for weight in weight_range:
        rocket = Rocket(thrust, weight, .65, 230, 9/12, .25)
        tuple = rocket.flight_simulation()
        print(tuple[5])
        oneD_res.append(tuple[5])
    x_twoD_res.append(oneD_res)


x_twoD_res = np.asarray(x_twoD_res)
X,Y = np.meshgrid(thrust_range,weight_range)
Z = x_twoD_res.reshape(X.shape)

ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
plt.show()




##
###Displacement subplot
##plt.subplot(2, 1, 1)
##plt.plot(tuple[2], tuple[0])
##plt.title('Displacement vs time')
##plt.ylabel('Displacement in feet')
###velocity subplot
##plt.subplot(2, 1, 2)
##plt.title('Velocity vs Time')
##plt.ylabel('Upwards velocity in feet/s')
##plt.xlabel('Time in seconds')
##plt.plot(tuple[2], tuple[1])
##
##plt.show()
