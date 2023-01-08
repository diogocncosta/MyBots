import pyrosim.pyrosim as pyrosim

#Measurements
length = 1
width = 1
height = 1

#this represent the position on where the world will appear initially 
x = -2
y = -2
z = 0.5

#this represent the position on where the robot will appear initially 
x1 = 0
y1 = 0
z1 = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[0, 0.5, 0.5] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, -0.5, -0.5])

    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0, 0] , size=[length, width, height])
    
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, 1.0, 0])

    pyrosim.Send_Cube(name="BackLeg", pos=[0, 0.5, -0.5] , size=[length, width, height])
    
    """
    pyrosim.Send_Cube(name="Link0", pos=[x1, y1, z1] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0, 0, 1.0])

    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0, 0, 1.0])

    pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0, 0.5, 0.5])

    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0] , size=[length, width, height])

    """
    
    pyrosim.End()

Create_World()
Create_Robot()
"""
for i in range(10):
    for j in range(5):
        for l in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x+l,y+j,z+i] , size=[length*0.90**i, width*0.90**i, height*0.90**i])
"""    

pyrosim.End()