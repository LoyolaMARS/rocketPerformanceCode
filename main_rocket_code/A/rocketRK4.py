## RocketRK4

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
# Diff Eq form:  a = (Thrust/mass) - 32.2ft/s^2 (or gravity) - (Cd*v^2)/mass
#                dv/dt = F(t,v)

def RK4(t, v, m, mDry, Cd, thrust, mDot, gravity, A, h):

####m2 for k2 and k3, in effect is t+(h/2)
    m2 = m - (mDot*h/2)
####m3 is for k4.  in effect is t+h
    m3 = m - mDot*h
    
    if (m > mDry):
        k1 = h*((thrust/m) - gravity - (.5 * A * .002377 * Cd/m * (v)**2))
        v2 = v + (k1/2)
        k2 = h*((thrust/m2) - gravity - (.5 * A * .002377 * Cd/m2 * (v2)**2))
        v3 = v + (k2/2)
        k3 = h*((thrust/m2) - gravity - (.5 * A * .002377 * Cd/m2 * (v3)**2))
        v4 = v + (k3)
        k4 = h*((thrust/m3) - gravity - (.5 * A * .002377 * Cd/m3 * (v4)**2))
        
        #print('engine on')
    else:   
        k1 = h*(0 - gravity - (.5 * A *  .002377 * Cd/m * (v)**2))
        v2 = v + (k1/2)
        k2 = h*(0 - gravity - (.5 * A *  .002377 * Cd/m2 * (v2)**2))
        v3 = v + (k2/2)
        k3 = h*(0 - gravity - (.5 * A *  .002377 * Cd/m2 * (v3)**2))
        v4 = v + (k3)
        k4 = h*(0 - gravity - (.5 * A *  .002377 * Cd/m3 * (v4)**2))
        
        #print('engine off')
    
    newVelocity = v + ((k1 + 2*k2 + 2*k3 + k4)/6 * h)
    #print('Velocity: ' + str(newVelocity))
    return newVelocity
