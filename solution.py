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
        #self.num = random.randint(1, 10)
        
        self.firstbranches = random.randint(1, 5)
        self.secondbranches = random.randint(0, self.firstbranches)
        
        self.nsensors = random.randint(1, self.firstbranches)
        print("firstgen=" + str(self.firstbranches))
        print("nsensors=" + str(self.nsensors))
        self.sensors = random.sample(range(0,self.firstbranches), self.nsensors)
        print("nsensors=" + str(self.sensors))

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
        length = 0.2
        #length = random.uniform(c.lowerBound, c.upperBound)
        width = random.uniform(c.lowerBound, c.upperBound) 
        height = random.uniform(c.lowerBound, c.upperBound)
        index = 0
        secondbranch = 1

        if index in self.sensors:
            pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, 0.5], size=[0.2, 0.2, 0.2], color="Green", rgba="0.0 1.0 0.0 1.0")
        else:
            pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, 0.5], size=[0.2, 0.2, 0.2], color="Cyan", rgba="0 1.0 1.0 1.0")
        
        # pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
        #     type = "revolute", position = [length/2, 0, 0.5], jointAxis= "0 0 1")
        
        for index in range(0, self.firstbranches):
            print(index)
            if index == 0:
                pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
                   type = "revolute", position = [length/2, 0, 0.5], jointAxis= "0 0 1")
            if index == 1:
                pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
                   type = "revolute", position = [-length/2, 0, 0.5], jointAxis= "0 0 1")
            if index == 2:
                pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
                   type = "revolute", position = [0, length/2, 0.5], jointAxis= "0 0 1")
            if index == 3:
                pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
                   type = "revolute", position = [0, -length/2, 0.5], jointAxis= "0 0 1")
            if index == 4:
                pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
                   type = "revolute", position = [0, 0, 0.5+length/2], jointAxis= "0 0 1")
            if index == 5:
                pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index+1), parent="Cube0", child ="Cube"+str(index+1),
                   type = "revolute", position = [0, 0, 0.5-length/2], jointAxis= "0 0 1")
        
        
        for index in range (0,self.firstbranches+1):
            self.cube(index, length)
        
        pyrosim.Send_Joint(name="Cube1"+"_Cube"+str(self.firstbranches+1), parent="Cube1", child ="Cube"+str(self.firstbranches+1),
                    type = "revolute", position = [0, 0.1, 0], jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="Cube"+str(self.firstbranches+1), pos=[0, 0.1, 0], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

    def create_random_sensors(self):

        num_sensors = self.sensors
        for i in range (self.nsensors):
            if i in num_sensors:
                pyrosim.Send_Sensor_Neuron(name = str(i), linkName = "Cube"+str(i))
    
    def cube(self, index, l):
        # pyrosim.Send_Joint(name="Cube0"+"_Cube"+str(index), parent="Cube0", child ="Cube"+str(index),
        #     type = "revolute", position = [length/2, 0, 0.5], jointAxis= "0 0 1")
        
        length = random.uniform(c.lowerBound, c.upperBound)
        width = random.uniform(c.lowerBound, c.upperBound) 
        height = random.uniform(c.lowerBound, c.upperBound)
        
        if index == 1:
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[l/2, 0, 0], size=[length, 0.2, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[l/2, 0, 0], size=[length, 0.2, height], color="Cyan", rgba="0 1.0 1.0 1.0")
            
        # pyrosim.Send_Joint(name="Cube1"+"_Cube"+str(index+self.firstbranches), parent="Cube1", child ="Cube"+str(index+self.firstbranches-1),
        #             type = "revolute", position = [0, 0, 0.5+length/2], jointAxis= "0 0 1")
        # pyrosim.Send_Cube(name="Cube"+str(index+self.firstbranches), pos=[length/2, 0, 0], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

        if index == 2:
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[-l/2, 0, 0], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[-l/2, 0, 0], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

        if index == 3:
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, l/2, 0], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, l/2, 0], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

        if index == 4:
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, -l/2, 0], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, -l/2, 0], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

        if index == 5:
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, l/2], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, l/2], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")

        if index == 6:
            if index in self.sensors:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, -l/2], size=[length, width, height], color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+str(index), pos=[0, 0, -l/2], size=[length, width, height], color="Cyan", rgba="0 1.0 1.0 1.0")






