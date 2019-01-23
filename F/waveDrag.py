#Computer new Cd as a function of mach number
#contributions by Harrison Leece, James Hribal
#Retruns new Cd based on the mach number of the rocket for wave drag effects

import numpy as np
import matplotlib.pyplot as plt

#compute mach number
def compMach(ftv,T):
    #convert v from ft/s to m/s
    v = ftv * .3048
    #R is kJ/(kg*K)
    R = .287
    #Specific heat ratio (gamma) is approx 1.4 for whole domain of temperatures
    gamma = 1.4
    #speed of sound = a, meters/s
    a = (gamma*R*1000*T)**.5
    mach = v/a
    return mach

#Takes in a altitude (in feet), converts to meters, then computes
#temperature in degrees C, which is then converted to kelvin
def compTemp(ftx):
    x = ftx*.3048
    if(x > 0 and x < 15354.016):
        C = 2.5574*10**(-7) * x**2 - 8.8754*10**(-3) *x + 18.1061
    elif(x > 15354.016 and x < 49697.695):
        C = 3.6838*10**(-8) * x**2 -7.6707*10**(-4) * x - 54.7841
    elif(x > 49697.695 and x < 120000):
        C = -2.4347*10**(-3) * x + 119.078
    else:
        C = -172
    T = C + 273.15
    return T

#Computes new Cd from the mach number of the rocket and initial Cd
def waveDrag(cd, mach):
    adj = cd - .3
    if(mach < .5085):
        nCd = .6827*mach**3 - .4297*mach**2 -.0358*mach + .3 + adj
    elif( mach > .5085 and mach < 1.3618):
        nCd = -0.7809*mach**4 + 2.324*mach**3 - 2.0189*mach**2 + 0.6793*mach + 0.1837 + adj
    elif(mach > 1.3618 and mach < 4):
        nCd = -.003495*mach**6+.07004*mach**5-.583*mach**4+2.564*mach**3-6.186*mach**2 + 7.466*mach -2.923 + adj
    else:
        nCd = .2184 + adj

    return nCd


#test plot
##cd = .25
##ncd = np.array([])
##mach = np.linspace(0,5,10000)
##for i in range(0,np.size(mach)):
##    ncd = np.append(ncd ,waveDrag(cd,mach[i]))
##
##plt.plot(mach,ncd)
##plt.show()
