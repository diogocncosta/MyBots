import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import numpy

class ROBOT:
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
    
    def Prepare_To_Act(self):
        self.motors = {}
        self.amplitude = numpy.pi/4
        self.frequency = 10
        self.offset = 0
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self,t):
        for jointName in self.motors:
            self.motors[jointName].Set_Value(self.robotId,t)

    def __init__(self):
        #self.motors = MOTOR()
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId) 
        self.Prepare_To_Sense()
        self.Prepare_To_Act()


      
        