from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c
import world as w
import robot as r
import sensor as s
import motor as m

class SIMULATION:

	def __init__(self, directOrGUI, solutionID):
		self.directOrGUI = directOrGUI
		if self.directOrGUI == "DIRECT":
			self.physicsClient = p.connect(p.DIRECT)
		else:
			self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		self.world = w.WORLD()
		self.robot = r.ROBOT(solutionID)
		p.setGravity(0,0,-9.8)

		


	
	def Run(self):
		for i in range(c.iterations):
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act(i)
			if self.directOrGUI == "GUI":
				# time.sleep(1/6000)
				pass

	def Get_Fitness(self):
		self.robot.Get_Fitness()


	def __del__(self):
		# for sensor in self.robot.sensors:
		# 	self.robot.sensors[sensor].Save_Values()
		# for motor in self.robot.motors:
		# 	self.robot.motors[motor].Save_Values()
		p.disconnect()