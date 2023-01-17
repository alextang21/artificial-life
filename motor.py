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



	def Set_Value(self, robot, desiredAngle):
		pyrosim.Set_Motor_For_Joint(

				bodyIndex = robot.robotId,

				jointName = self.jointName,

				controlMode = p.POSITION_CONTROL,

				targetPosition = desiredAngle,

				maxForce = c.legForce)

	def Save_Values(self):
		numpy.save("data/" + str(self.jointName)[2:-1] + "MotorData", self.motorValues)