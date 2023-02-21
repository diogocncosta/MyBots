import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1 
        self.weights = self.weights*20-1
        self.myID = nextAvailableID
        self.num = random.randint(0, 10)
        self.nsensors = random.randint(0, self.num)
        self.sensors = random.sample(range(1,self.num), self.nsensors)

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
        fx.close()
        fy.close()
        os.system("del" + " " + "fitnessx" + str(self.myID) + ".txt")
        os.system("del" + " " + "fitnessy" + str(self.myID) + ".txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        self.create_random_cubes()
        pyrosim.End()
        

    def Create_Brain(self):
        brainID = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainID)
        self.create_random_sensors()
        
        for currentRow in range(self.nsensors):
            for currentColumn in range(self.nsensors):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn, weight= self.weights[currentRow][currentColumn])
        pyrosim.End()


    def Mutate(self):
        randRow = random.randint(0,c.numSensorNeurons-1)
        randColumn = random.randint(0,c.numMotorNeurons-1)
        self.weights[randRow,randColumn] = random.random() * 2 - 1 


    def create_random_cubes(self):
        length = random.uniform(c.lowerBound, c.upperBound)
        width = random.uniform(c.lowerBound, c.upperBound) 
        height = random.uniform(c.lowerBound, c.upperBound)
        index = 0

        if index in self.sensors:
            pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, 0.5], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
        else:
            pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, 0.5], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

        pyrosim.Send_Joint(name="Cube"+str(index)+"_Cube"+str(index+1), parent="Cube"+str(index), child ="Cube"+str(index+1),
                     type = "revolute", position = [length/2, 0, 0.5], jointAxis= "0 0 1")

        for index in range(1, self.num):
            
            length = random.uniform(c.lowerBound, c.upperBound)
            width = random.uniform(c.lowerBound, c.upperBound) 
            height = random.uniform(c.lowerBound, c.upperBound)
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[length/2, 0, 0], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[length/2, 0, 0], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

            if index != self.num-1:
                pyrosim.Send_Joint(name="Cube"+str(index)+"_Cube"+str(index+1), parent="Cube"+str(index), child ="Cube"+str(index+1),
                    type = "revolute", position = [length, 0, 0], jointAxis= "0 0 1")

    def create_random_sensors(self):
        num_cubes = self.num
        num_sensors = self.sensors
        for i in range (self.nsensors):
            if i in num_sensors:
                pyrosim.Send_Sensor_Neuron(name = str(i), linkName = "Cube"+str(i))
        print("num_cubes" + str(num_cubes))
        print("which_sensors" + str(num_sensors))






