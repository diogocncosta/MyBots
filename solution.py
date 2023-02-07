import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1 
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
        
        while not os.path.exists("fitnessx" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        fx = open("fitnessx" + str(self.myID) + ".txt", "r")
        fy = open("fitnessy" + str(self.myID) + ".txt", "r")
        self.fitnessx = float(fx.read().strip('\n'))
        self.fitnessy = float(fy.read().strip('\n'))
        #print(self.fitness)
        fx.close()
        fy.close()
        os.system("del" + " " + "fitnessx" + str(self.myID) + ".txt")
        os.system("del" + " " + "fitnessy" + str(self.myID) + ".txt")

    # def Evaluate(self, directOrGUI):
    #     #os.system("python .\simulate.py " + directOrGUI + "&")
    #     pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-1, 2, 1.25] , size=[1, 1, 2.5])
        pyrosim.Send_Cube(name="Box", pos=[0, 2, 2.75] , size=[3, 1, 0.5])
        pyrosim.Send_Cube(name="Box", pos=[1, 2, 1.25] , size=[1, 1, 2.5])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1] , size=[1, 1, 1])
        
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.125, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.125, 0.5, 0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.125, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0.125, -0.5, 0] , size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name = "Torso_FrontLegv2" , parent= "Torso" , child = "FrontLegv2" , type = "revolute", position = [-0.125, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLegv2", pos=[-0.125, 0.5, 0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name = "Torso_BackLegv2" , parent= "Torso" , child = "BackLegv2" , type = "revolute", position = [-0.125, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLegv2", pos=[-0.125, -0.5, 0] , size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [0.5, 0.125, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0.125, 0] , size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [-0.5, 0.125, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0.125, 0] , size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name = "Torso_LeftLegv2" , parent= "Torso" , child = "LeftLegv2" , type = "revolute", position = [0.5, -0.125, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLegv2", pos=[0.5, -0.125, 0] , size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name = "Torso_RightLegv2" , parent= "Torso" , child = "RightLegv2" , type = "revolute", position = [-0.5, -0.125, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLegv2", pos=[-0.5, -0.125, 0] , size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0.125, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.125, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLegv2" , parent= "FrontLegv2" , child = "FrontLowerLegv2" , type = "revolute", position = [-0.125, 1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLegv2", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLegv2" , parent= "BackLegv2" , child = "BackLowerLegv2" , type = "revolute", position = [-0.125, -1, 0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLegv2", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [1, 0.125, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [-1, 0.125, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLegv2" , parent= "LeftLegv2" , child = "LeftLowerLegv2" , type = "revolute", position = [1, -0.125, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLegv2", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLegv2" , parent= "RightLegv2" , child = "RightLowerLegv2" , type = "revolute", position = [-1, -0.125, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLegv2", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        pyrosim.End()
        
    def Create_Brain(self):
        brainID = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainID)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        #pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLowerLeg")

        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLegv2")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLegv2")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLegv2")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLegv2")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "BackLowerLegv2")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "FrontLowerLegv2")
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "LeftLowerLegv2")
        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "RightLowerLegv2")

        pyrosim.Send_Motor_Neuron(name = 13 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 14 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 15 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 16 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name = 17 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 18 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 19 , jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 20 , jointName = "RightLeg_RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name = 21 , jointName = "Torso_BackLegv2")
        pyrosim.Send_Motor_Neuron(name = 22 , jointName = "Torso_FrontLegv2")
        pyrosim.Send_Motor_Neuron(name = 23 , jointName = "Torso_LeftLegv2")
        pyrosim.Send_Motor_Neuron(name = 24 , jointName = "Torso_RightLegv2")
        pyrosim.Send_Motor_Neuron(name = 25 , jointName = "BackLeg_BackLowerLegv2")
        pyrosim.Send_Motor_Neuron(name = 26 , jointName = "FrontLeg_FrontLowerLegv2")
        pyrosim.Send_Motor_Neuron(name = 27 , jointName = "LeftLeg_LeftLowerLegv2")
        pyrosim.Send_Motor_Neuron(name = 28 , jointName = "RightLeg_RightLowerLegv2")
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn + 18, weight= self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0,c.numSensorNeurons-1)
        randColumn = random.randint(0,c.numMotorNeurons-1)
        self.weights[randRow,randColumn] = random.random() * 2 - 1 
