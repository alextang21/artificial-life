import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import os
import constants as c

class SOLUTION:
	def __init__(self, myID):
		self.numSensorNeurons = random.randint(3,10)
		# self.numSensorNeurons = 3
		if self.numSensorNeurons % 2 == 0:
			self.numSensorNeurons += 1
		self.numMotorNeurons = self.numSensorNeurons + 1
		self.weights = numpy.random.rand(self.numSensorNeurons,self.numMotorNeurons)
		self.weights = self.weights * 2 - 1
		self.myID = myID

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Generate_Body()
		self.Generate_Brain()
		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

	def Wait_For_Simulation_To_End(self):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.01)
		f = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(f.read())
		f.close()
		os.system("rm fitness" + str(self.myID) + ".txt")

	def Evaluate(self, directOrGUI):
		self.Start_Simulation(directOrGUI)
		self.Wait_For_Simulation_To_End()

	def Mutate(self):
		self.weights[random.randint(0,2)][random.randint(0,1)] = random.random() * 2 - 1

	def Set_ID(self, ID):
		self.myID = ID

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[2,-3,0.5] , size=[1,1,1])
		pyrosim.End()

	def Generate_Body(self):
		pyrosim.Start_URDF(f"body{self.myID}.urdf")
		pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[1,0.5,0.5], color="Black", colorRGBA=[0,0,0,1.0])
		pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[-0.5,0,0.5], jointAxis = "0 0 1")
		pyrosim.Send_Cube(name="BackLeg1", pos=[-0.5,0,0] , size=[1,0.5,0.5], color="Cyan", colorRGBA=[0,1.0,1.0,1.0])
		pyrosim.Send_Joint(name="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[0.5,0,0.5], jointAxis = "0 0 1")
		pyrosim.Send_Cube(name="FrontLeg1", pos=[0.5,0,0] , size=[1,0.5,0.5], color="Cyan", colorRGBA=[0,1.0,1.0,1.0])
		for i in range(1, self.numMotorNeurons-1):
			if i % 2 == 1:
				pyrosim.Send_Joint(name=f"FrontLeg{i}_FrontLeg{i+1}", parent=f"FrontLeg{i}", child=f"FrontLeg{i+1}", type="revolute", position=[1,0,0], jointAxis = "0 0 1")
				pyrosim.Send_Cube(name=f"FrontLeg{i+1}", pos=[0.5,0,0] , size=[1,0.5,0.5], color="Black", colorRGBA=[0,0,0,1.0])
			else:
				pyrosim.Send_Joint(name=f"FrontLeg{i}_FrontLeg{i+1}", parent=f"FrontLeg{i}", child=f"FrontLeg{i+1}", type="revolute", position=[1,0,0], jointAxis = "0 0 1")
				pyrosim.Send_Cube(name=f"FrontLeg{i+1}", pos=[0.5,0,0] , size=[1,0.5,0.5], color="Cyan", colorRGBA=[0,1.0,1.0,1.0])
				
		# pyrosim.Send_Joint(name="FrontLeg1_FrontLeg2", parent="FrontLeg1", child="FrontLeg2", type="revolute", position=[1,0,0], jointAxis = "0 0 1")
		# pyrosim.Send_Cube(name="FrontLeg2", pos=[0.5,0,0] , size=[1,0.5,0.5], color="Black", colorRGBA=[0,0,0,1.0])
		# pyrosim.Send_Joint(name="FrontLeg2_FrontLeg3", parent="FrontLeg2", child="FrontLeg3", type="revolute", position=[1,0,0], jointAxis = "0 0 1")
		# pyrosim.Send_Cube(name="FrontLeg3", pos=[0.5,0,0] , size=[1,0.5,0.5], color="Cyan", colorRGBA=[0,1.0,1.0,1.0])

		pyrosim.End()

	def Generate_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "BackLeg1")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLeg1")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg3")
		sensorName = 3
		if self.numSensorNeurons > 3:
			for i in range(3,self.numSensorNeurons):
				if i % 2 == 0:
					pyrosim.Send_Sensor_Neuron(name = sensorName , linkName = f"FrontLeg{i+1}")
					sensorName += 1
		
		pyrosim.Send_Motor_Neuron( name = sensorName, jointName = "Torso_BackLeg1")
		pyrosim.Send_Motor_Neuron( name = sensorName + 1 , jointName = "Torso_FrontLeg1")
		pyrosim.Send_Motor_Neuron( name = sensorName + 2 , jointName = "FrontLeg1_FrontLeg2")
		pyrosim.Send_Motor_Neuron( name = sensorName + 3 , jointName = "FrontLeg2_FrontLeg3")
		motorName = numpy.array([3,4])
		if self.numMotorNeurons > 4:
			for i in range(4, self.numMotorNeurons):
				pyrosim.Send_Motor_Neuron( name = sensorName + i , jointName = f"FrontLeg{motorName[0]}_FrontLeg{motorName[1]}")
				motorName = motorName + 1

		for currentRow in range(self.numSensorNeurons):
			for currentColumn in range(self.numMotorNeurons):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + sensorName , weight = self.weights[currentRow][currentColumn] )

		pyrosim.End()








