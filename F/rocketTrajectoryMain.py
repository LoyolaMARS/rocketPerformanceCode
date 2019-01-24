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
import numpy as np
import matplotlib.pyplot as plt



rocket = Rocket(3000, 330, .65, 220, 9/12, .25)
tuple = rocket.flight_simulation()

print(tuple[5])

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
