from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import os
import constants as c
import sensor as s
import motor as m

class ROBOT:

	def __init__(self, ID):
		self.fileID = ID
		self.nn = NEURAL_NETWORK("brain" + str(ID) + ".nndf")
		# os.system("rm brain" + str(ID) + ".nndf")
		self.motors = {}
		self.robotId = p.loadURDF("body.urdf")
		self.lowerSensors = ["BackLowerLeg", "FrontLowerLeg", "LeftLowerLeg", "RightLowerLeg"]
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = s.SENSOR(linkName)

	def Sense(self,i):
		for sensor in self.lowerSensors:
			self.sensors[sensor].Count_Value(i)

	def Prepare_To_Act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = m.MOTOR(jointName)
		
	def Act(self, i):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[bytes(jointName, encoding='utf-8')].Set_Value(self, desiredAngle * c.motorJointRange)

	def Get_Fitness(self):
		
		meanTime = 0
		for i in self.lowerSensors:
			meanTime += numpy.mean(self.sensors[i].counter)
		# basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
		# basePosition = basePositionAndOrientation[0]
		# xPosition = basePosition[0]
		f = open("tmp" + str(self.fileID) + ".txt", "w")
		f.write(str(meanTime))
		f.close()
		os.system("mv tmp" + str(self.fileID) + ".txt fitness" + str(self.fileID) + ".txt")
		# f = open("fitness" + str(self.fileID) + ".txt", "w")
		# f.write(str(xCoordinateOfLinkZero))
		# f.close()

	def Think(self):
		self.nn.Update()
		# self.nn.Print()
