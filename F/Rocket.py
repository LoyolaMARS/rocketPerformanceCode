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
 *  1.0.1  2019-01-19  Harrison L.   Changed all vars to conform with python programming guidelines
 *  1.0.2  2019-01-19  Harrison L.   expanded Rocket init to return mdot and cd
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

#Create a Rocket Class
class Rocket():

    def __init__(self,thrust_input, weight, pr_ratio, isp, diameter, drag_coefficient):
        '''    weight :            total rocket weight
             pr_ratio :          mass of propelants / total wet mass of rockets
             isp :               specific impulse; rating of rocket efficiency
             diameter:           rocket body
             drag_coefficient:   coefficient of drag
        '''
        self.thrust = thrust_input
        self.gravity = 32.174  # ft / s^2
        self.initial_mass = weight / self.gravity
        self.propellant_mass = pr_ratio * self.initial_mass
        self.final_mass = self.initial_mass - self.propellant_mass
        self.area = 3.1416 * 1/4 * (diameter) ** 2
        self.m_dot = thrust_input/(isp*self.gravity)
        self.cd = drag_coefficient
        self.pr_ratio = pr_ratio


    def flight_simulation(self):

        gravity = 32.174  # ft / s^2
        step_size = .01
        #initialize rocket data from __init__
        thrust = self.thrust
        m_dot = self.m_dot
        area = self.area
        cd = self.cd
        pr_ratio = self.pr_ratio
        initial_mass = self.initial_mass
        propellant_mass = self.propellant_mass
        final_mass = self.final_mass


        mass = initial_mass

        #Initializes a bunch of stuff locally
        x_graph = np.array([0])
        v_graph = np.array([0])
        t_graph = np.array([0])

        #Generally, do not change these.  Describes initial conditions and
        #initializes the variables
        t=0
        v=0
        x = 0
        rho=0
        bo_time = 0
        bo_velocity = 0
        current_velocity = 0


        #While loop runs until rocket velocity is less than 10 feet/s
        while ((v > 10) or (t < 10)):
            #Calculates atmospheric density at altitude x and passes density to RK4 fxn.
            rho = compDensity(x)
            #Calculates mDot and thrust as tank pressure drops (if applicable) and  altitude changes
            n_thrust, n_mdot = compThrust2(thrust, m_dot, (initial_mass * pr_ratio), propellant_mass)
            #Calculates Cd as a fx of mach number
            K = compTemp(x)
            mach = compMach(v,K)
            n_cd = waveDrag(cd,mach)

            #RK4 function to solve rocket differential equation.  Returns v(t) approximated using Runge-Kutta 4th order method
            v = RK4(t,v, mass, final_mass, n_cd, n_thrust, n_mdot, gravity, area, step_size, rho)
            #Computes current displacement using reimen sum
            x = x + ((current_velocity + v)/2 * step_size)



            if (n_thrust > 0):
                mass = mass - n_mdot * step_size
                propellant_mass = propellant_mass - n_mdot * step_size
                bo_time = t
                bo_velocity = v
                bo_thrust = n_thrust
                bo_mdot = n_mdot
                bo_alt = x
            #Thrust is off, but propellant is still being drained by the tank pressue fluid (if applicable, such as blowdown system)
            elif (n_thrust == 0 and n_mdot != 0):
                mass = mass - n_mdot * step_size
                propellant_mass = propellant_mass - n_mdot * step_size
            else:
                #Leave this for clarity, though redundant
                mass = mass

            x_graph = np.append(x_graph, x)
            v_graph = np.append(v_graph, v)
            current_velocity = v

            #steps the while loop forward in time
            t = t + step_size
            t_graph = np.append(t_graph,t)


        #returns a tuple containing vectors containing displacement, velocity and time, maximum velocity, burnouttime, and max altitude
        return x_graph, v_graph, t_graph, bo_velocity, bo_time, x,
