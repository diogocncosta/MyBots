import pyrosim.pyrosim as pyrosim


pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

#this represent the position on where the cube will appear initially on the world
x = 0
y = 0
z = 0.5

for i in range(10):
    for j in range(5):
        for l in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x+l,y+j,z+i] , size=[length*0.90**i, width*0.90**i, height*0.90**i])
    

pyrosim.End()