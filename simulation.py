import pyrosim.pyrosim as pyrosim
import time as t 
import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
import constants as c


class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        #physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)    
        self.world = WORLD()
        self.robot = ROBOT()
        
    def __del__(self):
        p.disconnect()
    
    def run(self):
        for i in range(c.duration):
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                t.sleep(1/1000)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

        


        
