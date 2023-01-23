import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointname):
        self.jointname = jointname
        self.amplitude = 0
        self.frequency = 0
        self.offset = 0
        self.motorValues = {}
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = numpy.pi/4
        self.frequency = 10
        self.offset = 0
        self.motorValues = numpy.linspace(-numpy.pi, numpy.pi, 1000)
        self.motorValues = self.amplitude * numpy.sin(self.frequency * self.motorValues + self.offset)
        
    def Set_Value(self,robotID,t):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = self.jointname,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues[t],
        maxForce = 50)
    
    def Save_Values(self):
        numpy.save('/Users/Home/Documents/MyBots/data/MotorValuesdata.npy', self.motorValues)
    


        