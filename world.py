import pybullet as p

class WORLD:
    def __init__(self, solutionId):
        self.planeId = p.loadURDF("plane.urdf")
        #self.objects = p.loadSDF("world.sdf")
        p.loadSDF("world" + str(solutionId) + ".sdf")