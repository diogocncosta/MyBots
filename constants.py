import numpy as numpy

duration = 1000
numberOfGenerations = 1
populationSize = 1
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