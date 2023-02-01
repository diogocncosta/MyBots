import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

#Measurements
length = 1
width = 1
height = 1

#this represent the position on where the world will appear initially 
x = -2
y = -2
z = 0.5

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights*2-1
        self.myID = nextAvailableID
    
    def Set_ID(self, ID):
        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python simulate.py " + directOrGUI +  " " + str(self.myID)  + " &")
        
    def Wait_For_Simulation_To_End(self):
        
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read().strip('\n'))
        print(self.fitness)
        f.close()
        os.system("del" + " " + "fitness" + str(self.myID) + ".txt")

    # def Evaluate(self, directOrGUI):
    #     #os.system("python .\simulate.py " + directOrGUI + "&")
    #     pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5] , size=[length, width, height])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[length, width, height])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5] , size=[length, width, height])
        pyrosim.End()

    def Create_Brain(self):
        brainID = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainID)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn +3, weight= self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,2)
        randColumn = random.randint(0,1)
        self.weights[randRow,randColumn] = random.random() * 2 - 1 
