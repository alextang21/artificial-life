import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c
import sensor as s
import motor as m

class ROBOT:

	def __init__(self):
		self.motors = {}
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = s.SENSOR(linkName)

	def Sense(self,i):
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(i)

	def Prepare_To_Act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = m.MOTOR(jointName)
		
	def Act(self, i):
		for motor in self.motors:
			self.motors[motor].Set_Value(self,i)
