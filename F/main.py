#Rocket performance simulation main
from rocket import rocket
from rocket import flight_simulation



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
