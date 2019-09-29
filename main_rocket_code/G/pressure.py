import matplotlib.pyplot as plt
import numpy as np

def press(alt):
    '''@author Hannah Lane
    @param alt, The altitude the rocket is at
    @return pressure, the absolute pressure of the atmosphere at the
            rocket's altitude in psia
    '''
    pressure = 14.7*np.exp((-0.366713637542122*10**-4)*alt+(-0.000001623765497*10**(-4)*alt**2+(0.000000000007584*10**(-4)*alt**3)))
    return pressure


if __name__=="__main__":
    '''@author Hannah Lane
    Testing block for the pressure function

    '''
    alts = np.linspace(0,150000, 10000)
    pressure_vector = np.array([])
    for alt in alts:
        pressure = press(alt)
        pressure_vector = np.append(pressure_vector, pressure)


    plt.plot(alts, pressure_vector)

    plt.xlabel("Pressure")
    plt.ylabel("Altitude")
    plt.show()
