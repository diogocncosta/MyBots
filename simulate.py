import pybullet_data
import pybullet as p
import time as t 


physicsClient = p.connect(p.GUI)


p.setAdditionalSearchPath(pybullet_data.getDataPath())

#adds gravity to our world, in this case, box.sdf
p.setGravity(0,0,-9.8) 

#adds a floor to our world
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")



for i in range(1000):
    p.stepSimulation()
    t.sleep(1/60)
    print(i)
    
p.disconnect()