## Atmospheric density curve fit from Engineering Toolbox US standard Atmosphere
## Design by Harrison Leece, and the mathematics stackexchange

from scipy import optimize
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#magic stack exchange function
def seMagic(alt):
    s = -.2457039080*(alt/10**4)**1 -.0351850842 *(alt/10**4)**2 + 0.0021044026 *(alt/10**4)**3 - 0.0000390562*(alt/10**4)**4
    return 23.77 * 10**(-4) * np.exp(s)

############################################################################################################################################################################################################
# Everything below this line was for developement of the above function.  It is not strictly necessary
############################################################################################################################################################################################################
##altitudes = np.array([-5000,0,5000,10000,15000,20000,25000,30000,35000,40000,40001,45000,45001,50000,60000,70000,80000,90000,100000,150000,200000,250000])
##density1 = np.array([27.45,23.77,20.48,17.56,14.96,12.67,10.66,8.91,7.38,5.87,5.87,4.62,4.62,3.64,2.26,1.39,.86,.56,.33,.037,.0053,.00065])
##
##altitudeLinSpace = np.linspace(0,500000,500000)
##output = np.zeros(500000)

#stackexchange curve logic
#np.size(altitudeLinSpace)
##for i in range(0, np.size(altitudeLinSpace),1):
##    output[i] = seMagic(altitudeLinSpace[i])
## 
##print(output)
##
##
###Plots data
##plt.grid(True)
##plt.ylim((0,25))
##plt.ylabel('Density of atmospher in slug/ft^3 * 10^-4')
##plt.xlabel('Altitude, feet')
###Data from engineering toolbox
##plt.plot(altitudes, density1)
###stackexchange curve fit
##plt.plot(altitudeLinSpace, output)
##
##plt.show()
