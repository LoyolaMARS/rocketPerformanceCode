''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * File name  :  RocketFlightCharacteristics.java
 * Purpose    :  To Characterize the motion of a rocket given certain values using numerical methods.
 * @author    :  Harrison Leece, Bailey Paige
 * @author    :  Debugged by Matt Abel, Max Fung, Matthew Stein
 * Date       :  2019-01-17
 * Notes      :  None
 * Warnings   :  None
 *
 *  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * Revision History
 * ================
 *   Ver      Date     Modified by:  Reason for change or modification
 *  -----  ----------  ------------  ---------------------------------------------------------------------
 *  1.0.0  2019-01-17  Matt Stein    Harrison Leece original code updates loaded in
 *  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
 # imports
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

# Create a Rocket Class
class Rocket:

     def __init__(weight, pr_ratio, isp, diameter, drag_coefficient):
         '''    weight :            total rocket weight
                pr_ratio :          mass of propelants / total wet mass of rockets
                isp :               specific impulse; rating of rocket efficiency
                diameter:           rocket body
                drag_coefficient:   coefficient of drag
         '''
         gravity = 32.174  # ft / s^2
         initial_mass = weight / gravity
         propellant_mass = pr_ratio * initial_mass
         final_mass = initial_mass - propellant_mass
         area = 3.1416 * 1/4 * (diameter) ** 2

         return gravity, initial mass, propellant_mass, final_mass, area

        ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ## ADDITIONAL CODE TO BE SORTED


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


    ## END ADDITIONAL CODE TO BE SORTED
    ## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

         '''
         STILL READING THROUGH THE SIMULATION CODE TO UNDERSTAND HOW IT WORKS.
         GOAL IS TO CREATE A ROCKET OBJECT THAT UNDERGO A SIMULATED FLIGHT
         THE FLIGHT SIMULATION IS A FUNCTION.
         '''
     def flight_simulation( ):
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
