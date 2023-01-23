from simulation import SIMULATION
simulation = SIMULATION()
simulation.run()

"""
import pybullet as p
import pybullet_data
import time as t 
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random as random
import constants as c

#physicsClient = p.connect(p.GUI)

#p.setAdditionalSearchPath(pybullet_data.getDataPath())

#adds gravity to our world, in this case, box.sdf
#p.setGravity(0,0,-9.8) 

#adds a floor to our world
#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")

#numpy.save('/Users/Home/Documents/MyBots/data/FtargetAngles.npy', FtargetAngles)
#numpy.save('/Users/Home/Documents/MyBots/data/BtargetAngles.npy', BtargetAngles)

#pyrosim.Prepare_To_Simulate(robotId)
for i in range(1000):
    p.stepSimulation()

    #Sensors
    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    #Motors
    #backleg
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b"Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = c.BtargetAngles[i],
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

p.disconnect()
#print(backLegSensorValues)
numpy.save('/Users/Home/Documents/MyBots/data/backLegSensorValuesdata.npy', backLegSensorValues)
numpy.save('/Users/Home/Documents/MyBots/data/frontLegSensorValuesdata.npy', frontLegSensorValues)
"""