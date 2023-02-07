import numpy 
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self, linkname):
        self.linkname = linkname
        self.values = numpy.zeros(1000)
    
    def Get_Value(self,i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)

    def Save_Values(self):
        numpy.save('/Users/Home/Documents/MyBots/data/SensorValuesdata.npy', self.values)

