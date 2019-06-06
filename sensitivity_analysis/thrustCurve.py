#Function to calculate new mDot and thrust as tanks depressurize
#Design by Harrison Leece

import numpy as np
import matplotlib.pyplot as plt

#ALL MASSES ARE PROPELLANT MASSES
def newThrustMdot(initialThrust,initialMdot, inMass, curMass):
    #a linear relationship between tank pressure and mDot is assumed
    #Then a linear elationship between mDot is assumed
    #Mass of helium pressurant is considered neglegible
    #Therefore, a lienar relationship between current propellant mass and thrust
    #and mass flow rate can be established
    
    ratio = curMass/inMass
    nThrust = initialThrust * ratio
    #Remember: initialMdot is computed from thrust/(g*isp) outside of main while loop
    nMdot = initialMdot * ratio
    
    #print(initialThrust)
    #print(nThrust)
    #print(nMdot)
    
    #Very important peice of logic; I assume thrust will cut out before tanks are dry
    #Because gasses will not attain sonic velocity at throat
    #Turns off thrust, which will then control RK4 and burnout time logic.
    if nMdot< (.1 * initialMdot):
        nThrust = 0
    if (nMdot < .0002):
        nMdot = 0
    return nThrust, nMdot

def pressurantThrust(initialThrust,initialMdot, inMass, curMass):
    thrust = initialThrust
    mDot = initialMdot
    if(curMass < .1):
        thrust = 0
        mDot = 0
    return thrust, mDot



#testing code for newThrustMdot
##t = 0
##tGraph = np.array([])
##iThrust = 2000
##g = 32.174
##isp = 230
##initialMdot = iThrust/(g*isp)
##initialMass = 95/g
##pM = initialMass
##h=.005
##
##mDot = 1
##thrustGraph = np.array([iThrust])
##tGraph = np.array([0])
##while (mDot > .002):
##
##    thrust, mDot = pressurantThrust(iThrust, initialMdot, initialMass, pM)
##    pM = pM - mDot * h
##    tGraph = np.append(tGraph,t)
##    t = t + h
##    thrustGraph = np.append(thrustGraph,thrust)
##
##plt.title('Thrust curve')
##plt.ylabel('Thrust, lbs')
##plt.xlabel('Time in seconds, step is .005')
##plt.plot(tGraph,thrustGraph)
##plt.show()
