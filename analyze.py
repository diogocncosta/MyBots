import matplotlib.pyplot as plt
import numpy as numpy
backLegSensorValues = numpy.load('/Users/Home/Documents/MyBots/data/backLegSensorValuesdata.npy')
frontLegSensorValues = numpy.load('/Users/Home/Documents/MyBots/data/frontLegSensorValuesdata.npy')
BtargetAngles = numpy.load('/Users/Home/Documents/MyBots/data/BtargetAngles.npy')
FtargetAngles = numpy.load('/Users/Home/Documents/MyBots/data/FtargetAngles.npy')
#print(backLegSensorValues)
#print(frontLegSensorValues)

plt.plot(BtargetAngles)
plt.plot(FtargetAngles)


plt.plot(backLegSensorValues, label='backLegSensor', linewidth=2.5)
plt.legend()
plt.plot(frontLegSensorValues, label='frontLegSensor')
plt.legend()
plt.show()