#Coefficient of Drag vs mach number function
#Design by Harrison Leece

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def poly4thO(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e
def poly2ndO(x,a,b):
    return a*x**2 + b*x + .3


#Takes in initial Cd and current mach number and returns the Cd
def comDrag(Cd, m):

    if m < .2386:
        return poly2ndO(m,.24410868,-.17506498)
    else:
        return poly4thO(m,-0.50610628,1.27858717, -0.65259596, -0.02275554, 0.29898371)
    nM = 0 

    return nM

#Curve fitting
#segment 1
y1 = np.array([.3,.3   ,.3   , .28     ,.275  ,.26  ,.265,.27 ,.335,.4,.51 ,.55])
x1 = np.array([ 0,.0001,.0001,.125  ,.25   ,.5   ,.625,.75 ,.825,1 ,1.25,1.5])
p, pc = curve_fit(poly2ndO,x1,y1)

print(p)
#Curve fitting
#segment 2
popt, pcov = curve_fit(poly4thO,x1,y1)
print (popt)
#Curve fitting 
#segment 3

x2 = np.arange(0,1.5,.001)
plt.plot(x1,y1)

plt.plot(x2,poly2ndO(x2, p[0], p[1]))

plt.plot(x2, poly4thO(x2,popt[0],popt[1],popt[2],popt[3],popt[4]))



plt.show()
