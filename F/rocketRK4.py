## RocketRK4, Harrison Leece
# t = time, ###Not currently used, important for future expansion###
# v = velocity
# m = mass,
# mFinal = Final mass of rocket, which is important for turning off
#          thrust and mass loss
# Cd = Coefficient of Drag, which is assumed constant, but is really
#      a function of height, but is assumed constant for simplicity
# thrust
# m2 = mass of fuel at 1/2 the step (for runge kutta 4th order k2 and k3 terms)
# h = stepSize
# Diff Eq form:  a = (Thrust/mass) - 32.2ft/s^2 (or gravity) - (.5*Area*rho)*(Cd*v^2)/mass
#                dv/dt = F(t,v); v is a fxn of time, mass is a fxn of t
#The RK4 method constitutes a "time step simulation"


def RK4(t, v, m, mDry, Cd, thrust, mDot, gravity, A, h,r):

####m2 for k2 and k3, in effect is t+(h/2)
    m2 = m - (mDot*h/2)
####m3 is for k4.  in effect is t+h
    m3 = m - mDot*h

    #Thrust is controlled by thrustCurve.py and will turn off when thrust
    #is approx half of initial
    # Try catch trades tiny speed increases for debugging efficiency
    try:
        k1 = h*((thrust/m) - gravity - (.5 * A * r * Cd/m * (v)**2))
        v2 = v + (k1/2)
        k2 = h*((thrust/m2) - gravity - (.5 * A * r * Cd/m2 * (v2)**2))
        v3 = v + (k2/2)
        k3 = h*((thrust/m2) - gravity - (.5 * A * r * Cd/m2 * (v3)**2))
        v4 = v + (k3)
        k4 = h*((thrust/m3) - gravity - (.5 * A * r * Cd/m3 * (v4)**2))
    except:
        print("\nlikely overflow:  current system properties print")
        print("Thrust: " +str(thrust))
        print("Mass: " + str(m))
        print("DryMass: " + str(mDry))
        print("Velocity: " + str(v))
        print("Atmospheric Density: " + str(r))
        print("Step Size sanity check: " + str(h))
        print("Time sanity check: " + str(t))

    newVelocity = v + ((k1 + 2*k2 + 2*k3 + k4)/6)

    #print('Velocity: ' + str(newVelocity))
    return newVelocity
