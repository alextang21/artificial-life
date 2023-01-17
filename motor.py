import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import constants as c

class MOTOR:

	def __init__(self, jointName):
		self.jointName = jointName
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		self.amplitude = c.amplitude
		self.frequency = c.frequency
		self.offset = c.offset
		print(str(self.jointName))
		if "back" in str(self.jointName).lower():
			self.motorValues = self.amplitude * numpy.sin(self.frequency/2 * (numpy.linspace(0, 2*numpy.pi, c.iterations)) + self.offset)*(numpy.pi/6)
		else:
			self.motorValues = self.amplitude * numpy.sin(self.frequency * (numpy.linspace(0, 2*numpy.pi, c.iterations)) + self.offset)*(numpy.pi/6)


	def Set_Value(self, robot, i):
		pyrosim.Set_Motor_For_Joint(

				bodyIndex = robot.robotId,

				jointName = self.jointName,

				controlMode = p.POSITION_CONTROL,

				targetPosition = self.motorValues[i],

				maxForce = c.legForce)

	def Save_Values(self):
		numpy.save("data/" + str(self.jointName)[2:-1] + "MotorData", self.motorValues)