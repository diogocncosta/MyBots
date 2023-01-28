import pyrosim.pyrosim as pyrosim
import time as t 
import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
import constants as c

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
    
    def __del__(self):
        p.disconnect()
    
    def run(self):
        for i in range(c.duration):
            #print(i)
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            t.sleep(1/60)
            """
            #Sensors
            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            #Motors
            #backleg
            pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b"Torso_BackLeg",
            controlMode = p.POSITION_CONTROL,
             = c.BtargetAngles[i],
            maxForce = 50)
    
            #frontleg
            pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b"Torso_FrontLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = c.FtargetAngles[i],
            maxForce = 50)

            t.sleep(1/60)
            print(i)
            """

        
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

        
