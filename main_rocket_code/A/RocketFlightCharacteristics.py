## Rocket calculations in python.
## Objective: Characterize the motion of a rocket given certain
##            values using numerical methods.
## Debugged by Matt Abel, Max Fung
import math
from rocketRK4 import RK4

# Inputs
# gravity, isp, atmosphere and thrust are assumed constant
# Units of mass should be in slug for imperial and kg for metric
gravity = 32.2
mass = (700/gravity)

#initialMass variable allows the mass of the rocket to be reset durring outer for loop
initialMass = mass

#Typical pressure-fed systems have a propellant weight to total weight ratio of
# .89  .80 is selected to be conservative
propellantMass = .85 * mass
finalMass = mass - propellantMass

#Kerosene LOX has a theoretical max ISP of ~360.  F1 engine is 263 ISP at sea level
#Therefore, an ISP of 240 at Sea Level is a conservative estimate
isp = 240

Area = 3.1416 * 1/4 * 1
# A Supersonic fighter has a Cd of .016.  Subsonic is .012 therefore
# A rocket = .05 if aerodynamics are done well
Cd = .05




#Step size of calculations.  Smaller number = higher precision
#Unit is seconds
stepSize = .05




# Passes curren time 'step' conditions to RK4 function
# Returns the next time 'step' conditions.
# Eqaution is modified in RK4.py file

range_thrust=range(0,6000,100)
print(range_thrust)
for thrust in range_thrust:
    #Generally, do not change these.  Describes initial conditions and
    #initializes the variables
    t=0
    v=0

    x = 0
    burnOutTime = 0
    burnOutVelocity = 0
    currentVelocity = 0
    
    mass = initialMass

    print('\nTHRUST TESTED: ' +str(thrust))
    #Establishes mDot from thrust, gravity and isp
    mDot = thrust/(gravity * isp)
    print(thrust)
    print(mDot)
    while (True):

        
        v = RK4(t,v, mass, finalMass, Cd, thrust, mDot, gravity, Area, stepSize)
        ####print('check 0')
        
        if v > 0:
            if (mass > finalMass):
                mass = mass - mDot * stepSize
                burnOutTime = t
                burnOutVelocity = v
            else:
                #Leave this for clarity, though redundant
                mass = mass
            #Computes current displacement
            x = x + ((currentVelocity + v)/2 * stepSize)
            currentVelocity = v
            #steps the while loop forward in time
            ####print('check' + str(t))
            t = t + stepSize
            #print(x)
           
            
        else:
            break

    print('Burnout at ' + str(burnOutTime) + ' feet')
    print('Burnout velocity ' + str(burnOutVelocity) + ' feet/seconds' )
    print(t)
    print(x)
            
