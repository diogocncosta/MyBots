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
    #Define the main cube
        pyrosim.Send_Cube(name="Cube0", pos=[0, 2, 0.5] , size=[1, 1, 1], color="Cyan", rgba="0 1.0 1.0 1.0")
        
    # Create a random number of cubes
        num_cubes = self.num
        for i in range(num_cubes):
            x=random.randint(1, 1)
            z=random.randint(1, 2)
            y=random.randint(1, 2)
            
            size = [x, y, z]
            pos = [x/2, 2, 0]
            
            if i in self.sensors:
                pyrosim.Send_Cube(name="Cube"+ str(i+1), pos=pos, size=size, color="Green", rgba="0.0 1.0 0.0 1.0")
            else:
                pyrosim.Send_Cube(name="Cube"+ str(i+1), pos=pos, size=size, color="Cyan", rgba="0 1.0 1.0 1.0")
            
            if i == 0:
                pyrosim.Send_Joint(name="Joint_Cube"+str(i)+"_Cube"+str(i+1), parent="Cube"+str(i), child="Cube"+str(i+1), type="revolute", position=[0.5, 0, 0.5], jointAxis="0 1 0")
            else:
                pyrosim.Send_Joint(name="Joint_Cube"+str(i)+"_Cube"+str(i+1), parent="Cube"+str(i), child="Cube"+str(i+1), type="revolute", position=[x, 0, 0], jointAxis="0 1 0")
            print(x, y, z)

    def create_random_sensors(self):
        num_cubes = self.num
        num_sensors = self.sensors
        for i in range (self.nsensors):
            if i in num_sensors:
                pyrosim.Send_Sensor_Neuron(name = str(i), linkName = "Cube"+str(i))
        print("num_cubes" + str(num_cubes))
        print("which_sensors" + str(num_sensors))






