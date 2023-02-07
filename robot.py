import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        brainID = "brain" + str(solutionID) + ".nndf"
        self.solutionID = solutionID
        #self.motors = MOTOR()
        self.nn = NEURAL_NETWORK(brainID)
        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}
        self.sensors = {}
        pyrosim.Prepare_To_Simulate(self.robotId) 
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del" + " " + "brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        #self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,t):
        for i in self.sensors.keys():
            self.sensors[i].Get_Value(t)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
    
    def Prepare_To_Act(self):
        #self.motors = {}
        self.amplitude = numpy.pi/4
        self.frequency = 10
        self.offset = 0
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self,t):
        
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                # print(neuronName, jointName, desiredAngle)
                self.motors[jointName].Set_Value(self.robotId,desiredAngle)
    
    def Get_Fitness(self):
        # stateOfLinkZero = p.getLinkState(self.robotId,0)
        # positionOfLinkZero = stateOfLinkZero[0]
        # xCoordinateOfLinkZero = positionOfLinkZero[0]

        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)

        basePosition = basePositionAndOrientation[0]

        xPosition = basePosition[0]
        yPosition = basePosition[1]
        
        #save x position
        f = open("tmpx" + str(self.solutionID) + ".txt", "w")
        f.write(str(xPosition))
        #f.write(str(xCoordinateOfLinkZero))
        f.close()

        #save y position
        f = open("tmpy" + str(self.solutionID) + ".txt", "w")
        f.write(str(yPosition))
        #f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmpx" + str(self.solutionID) + ".txt", "fitnessx"  + str(self.solutionID) + ".txt")
        os.rename("tmpy" + str(self.solutionID) + ".txt", "fitnessy"  + str(self.solutionID) + ".txt")
        #print(stateOfLinkZero)
        #print(positionOfLinkZero)
        exit()
    


      
        