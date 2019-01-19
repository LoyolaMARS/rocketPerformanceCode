## Rocket calculations in python, design by Harrison Leece and Bailey Page
## Objective: Characterize the motion of a rocket given certain
##            values using numerical methods.
## Debugged by Matt Abel, Max Fung

import math
import numpy as np
from rocketRK4 import RK4
import matplotlib.pyplot as plt
from atmosphereDensity import seMagic as compDensity
from thrustCurve import newThrustMdot as compThrust
from thrustCurve import pressurantThrust as compThrust2
from waveDrag import compTemp
from waveDrag import compMach
from waveDrag import waveDrag


# Inputs
# gravity, isp, atmosphere and thrust are assumed constant
# Units of mass should be in slug for imperial and kg for metric.
gravity = 32.174
#Mass 
mass = (330/gravity)
#initialMass variable allows the mass of the rocket to be reset durring outer for loop
initialMass = mass

#Typical pressure-fed systems have a propellant weight to total weight ratio of
# .89  .65 or less is more probable on amateur rockets
prRatio = .65
propellantMass = prRatio * mass
#finalMass is used to determine if the rocket is thrusting or not...
#I want to get rid of this variable and replace it with when mDot is 0 stop thrusting... soon
finalMass = (mass - propellantMass)
#Specific impulse
isp = 240
#10 inches diameter
diameter = 10/12
Area = 3.1416 * 1/4 * (diameter)**2
# Assume .25 at ground and low velocity
Cd = .25

#Step size of calculations.  Smaller number = higher precision
#Unit is seconds.  .01 is the size of Rick Loehr's step size
stepSize = .01

# Passes curren time 'step' conditions to RK4 function
# Returns the next time 'step' conditions.
# Eqaution is modified in RK4.py file


#range is to allow faster optimization of engine thrust if desired
range_thrust=range(3000,3001,250)
print(range_thrust)
#initialize graphing arrays
xGraph = np.array([0])
vGraph = np.array([0])
tGraph = np.array([0])
for thrust in range_thrust:

	#Generally, do not change these.  Describes initial conditions and
	#initializes the variables
	t=0
	v=0
	x = 0
	rho=0
	burnOutTime = 0
	burnOutVelocity = 0
	currentVelocity = 0

	mass = initialMass
	propellantMass = prRatio * mass



	print('\nTHRUST TESTED: ' +str(thrust))

	#Establishes mDot from thrust, gravity and isp
	mDot = thrust/(gravity * isp)
	print(thrust)
	print('Starting mDot: ' + str(mDot))

	while (True):
		#Calculates atmospheric density at altitude x and passes density to RK4 fxn.
		rho = compDensity(x)
		#Calculates mDot and thrust as tank pressure drops
		nThrust, nMdot = compThrust2(thrust, mDot, (initialMass * prRatio) , propellantMass)
		#Calculates Cd as a fx of mach number
		K = compTemp(x)
		mach = compMach(v,K)
		nCd = waveDrag(Cd,mach)
		#RK4 fxn
		v = RK4(t,v, mass, finalMass, nCd, nThrust, nMdot, gravity, Area, stepSize, rho)
		
		
		# Greater than 30 so that program will terminate when velocity is trivial
		# or t<10 to make sure loop does not break when object is first accelerating
		if (v > 30) or (t < 10):
			if (nThrust > 0 and (mass > finalMass)):
				mass = mass - nMdot * stepSize
				propellantMass = propellantMass - nMdot * stepSize
				burnOutTime = t
				burnOutVelocity = v
				thrustAtBO = nThrust
				nMdotAtBO = nMdot
				dispAtBO = x
			#Thrust is off, but propellant is still being drained by the pressurant fluid
			elif (nThrust == 0 and nMdot != 0):
				mass = mass - nMdot * stepSize
				propellantMass = propellantMass - nMdot * stepSize
			else:
				#Leave this for clarity, though redundant
				mass = mass
			#Computes current displacement using reimen sum
			x = x + ((currentVelocity + v)/2 * stepSize)

			xGraph = np.append(xGraph, x)
			vGraph = np.append(vGraph, v)
			currentVelocity = v

			#steps the while loop forward in time
			t = t + stepSize
			tGraph = np.append(tGraph,t)
		else:
			break

	print('Burnout at ' + str(burnOutTime) + ' seconds')
	print('Burnout disp: ' + str(dispAtBO) + 'feet')
	print('Burnout velocity ' + str(burnOutVelocity) + ' feet/seconds' )
	print('Thrust before BO: ' + str(thrustAtBO))
	print('mDot before BO: ' + str(nMdotAtBO) + '\n')
	print("Time to apopapsis: " + str(t))
	print('Displacement '+ str(x) + ' feet') #Added the label of displacement here... displacement or altitude?
	print("Goal displacement = " + str(5280 * 63) + "Feet ")
	print("Current mass - theoretical dry mass: " + str(mass - finalMass))



	plt.subplot(2, 1, 1)
	plt.plot(tGraph, xGraph)
	plt.title('Displacement vs time')
	plt.ylabel('Displacement in feet')

	plt.subplot(2, 1, 2)
	plt.title('Velocity vs Time')
	plt.ylabel('Upwards velocity in feet/s')
	plt.xlabel('Time in seconds')
	plt.plot(tGraph, vGraph)



plt.show()

