from pyrosim.neuralNetwork import NEURAL_NETWORK
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
		self.nn = NEURAL_NETWORK("brain.nndf")
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
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[bytes(jointName, encoding='utf-8')].Set_Value(self,desiredAngle)
				print(neuronName + "\n" + jointName + "\n" + str(desiredAngle))

		# for motor in self.motors:
		# 	self.motors[motor].Set_Value(self,i)

	def Think(self):
		self.nn.Update()
		self.nn.Print()
