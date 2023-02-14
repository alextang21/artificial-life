import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c

class SENSOR:

	def __init__(self, linkName):
		self.linkName = linkName
		self.values = numpy.zeros(c.iterations)
		self.counter = numpy.zeros(c.iterations)

	def Get_Value(self,i):
		self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) * numpy.sin(2*i)
	
	def Count_Value(self,i):
		self.counter[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def Save_Values(self):
		numpy.save("data/" + str(self.linkName) + "SensorData", self.values)