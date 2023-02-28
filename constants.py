import numpy as numpy

lowerBound = 0.1
upperBound = 0.4
duration = 300
numberOfGenerations = 10
populationSize = 5
motorJointRange = 0.2

numSensorNeurons = 9
numMotorNeurons = 8
#Motor Command Vector
#Backleg Variables
Bamplitude = numpy.pi/4
Bfrequency = 10
BphaseOffset = 0

BtargetAngles= numpy.linspace(-numpy.pi, numpy.pi, 1000)
BtargetAngles = Bamplitude * numpy.sin(Bfrequency * BtargetAngles + BphaseOffset)

#Frontleg Variables
Famplitude = numpy.pi/4
Ffrequency = 10
FphaseOffset = 0

FtargetAngles= numpy.linspace(-numpy.pi, numpy.pi, 1000)
FtargetAngles = Famplitude * numpy.sin(Ffrequency * FtargetAngles + FphaseOffset)