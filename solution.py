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
		self.limbs = {}
		self.num_limbs = [i for i in range(random.randint(2,5)*2+1)]
		self.sensors = numpy.random.randint(2, size = len(self.num_limbs))
		self.motors = numpy.random.randint(2, size = len(self.num_limbs))
		self.colors = {0: ["Blue", [0,0,1.0,1.0]], 1: ["Green", [0,1.0,0,1.0]]}
		self.motors[0] = 0
		
		self.weights = numpy.random.rand(numpy.count_nonzero(self.sensors == 1), numpy.count_nonzero(self.motors == 1))
		self.weights = self.weights * 2 - 1
		self.myID = myID
		# limbs is a dictionary
		# limbs: key is the number ID of the limb, value is a list with [sensor?, size[], color, colorRGBA]
		

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
		pass
		# self.weights[random.randint(0,numpy.count_nonzero(self.sensors == 1)-1)][random.randint(0,numpy.count_nonzero(self.motors == 1)-1)] = random.random() * 2 - 1

	def Set_ID(self, ID):
		self.myID = ID

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[2,-3,0.5] , size=[1,1,1])
		pyrosim.End()

	def Generate_Body(self):

		for i in range(len(self.num_limbs)):
			self.limbs[i] = [self.sensors[i], self.motors[i], numpy.random.rand(3) * random.randint(1,2)/2 + 1, self.colors[self.sensors[i]][0], self.colors[self.sensors[i]][1]]
		start_z = 0.0
		for i in self.limbs:
			start_z += self.limbs[i][2][2]

		start_z /= 2
		
		pyrosim.Start_URDF(f"body{self.myID}.urdf")
		pyrosim.Send_Cube(name=f"Segment0", pos=[0,0,start_z], size=self.limbs[0][2], color=self.limbs[0][3], colorRGBA=self.limbs[0][4])
		pyrosim.Send_Joint(name=f"Segment0_Segment1", parent=f"Segment0", child=f"Segment1",  type="revolute", position=[-self.limbs[0][2][0]/2,self.limbs[0][2][1]/2,start_z-(self.limbs[0][2][2]/4)], jointAxis = "0 1 1")
		pyrosim.Send_Joint(name=f"Segment0_Segment2", parent=f"Segment0", child=f"Segment2",  type="revolute", position=[-self.limbs[0][2][0]/2,-self.limbs[0][2][1]/2,start_z-(self.limbs[0][2][2]/4)], jointAxis = "0 1 1")
		for i in range(1,len(self.num_limbs)-2):
			directions = numpy.random.randint(2, size = 3)
			directions[2] = 1
			if i % 2 == 0:
				pyrosim.Send_Cube(name=f"Segment{i}", pos=[self.limbs[i][2][0]/2,-self.limbs[i][2][1]/2,-self.limbs[i][2][2]/4], size=self.limbs[i][2], color=self.limbs[i][3], colorRGBA=self.limbs[i][4])
				pyrosim.Send_Joint(name=f"Segment{i}_Segment{i+2}", parent=f"Segment{i}", child=f"Segment{i+2}",  type="revolute", position=[self.limbs[i][2][1]/2,-self.limbs[i][2][1]/2,-self.limbs[i][2][2]] * directions, jointAxis = "0 1 1")
			else:
				pyrosim.Send_Cube(name=f"Segment{i}", pos=[self.limbs[i][2][0]/2,self.limbs[i][2][1]/2,-self.limbs[i][2][2]/4], size=self.limbs[i][2], color=self.limbs[i][3], colorRGBA=self.limbs[i][4])
				pyrosim.Send_Joint(name=f"Segment{i}_Segment{i+2}", parent=f"Segment{i}", child=f"Segment{i+2}",  type="revolute", position=[self.limbs[i][2][1]/2,self.limbs[i][2][1]/2,-self.limbs[i][2][2]] * directions, jointAxis = "0 1 1")
		pyrosim.Send_Cube(name=f"Segment{self.num_limbs[-2]}", pos=[self.limbs[self.num_limbs[-2]][2][0]/2,self.limbs[self.num_limbs[-2]][2][1]/2,-self.limbs[self.num_limbs[-2]][2][2]/4], size=self.limbs[self.num_limbs[-2]][2], color=self.limbs[self.num_limbs[-2]][3], colorRGBA=self.limbs[self.num_limbs[-2]][4])
		pyrosim.Send_Cube(name=f"Segment{self.num_limbs[-1]}", pos=[self.limbs[self.num_limbs[-1]][2][0]/2,-self.limbs[self.num_limbs[-1]][2][1]/2,-self.limbs[self.num_limbs[-1]][2][2]/4], size=self.limbs[self.num_limbs[-1]][2], color=self.limbs[self.num_limbs[-1]][3], colorRGBA=self.limbs[self.num_limbs[-1]][4])

		pyrosim.End()

	def Generate_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		neuron_counter = 0
		for i in self.limbs:
			if self.limbs[i][0] == 1:
				pyrosim.Send_Sensor_Neuron(name = neuron_counter, linkName = f"Segment{i}")
				neuron_counter += 1
		
		for i in self.limbs:
			if self.limbs[i][1] == 1:
				if i == 1:
					pyrosim.Send_Motor_Neuron( name = neuron_counter, jointName = f"Segment{i-1}_Segment{i}")
					neuron_counter += 1
				else:
					pyrosim.Send_Motor_Neuron( name = neuron_counter, jointName = f"Segment{i-2}_Segment{i}")
					neuron_counter += 1

		for currentRow in range(numpy.count_nonzero(self.sensors == 1)):
			for currentColumn in range(numpy.count_nonzero(self.motors == 1)):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + numpy.count_nonzero(self.sensors == 1) , weight = self.weights[currentRow][currentColumn] )

		pyrosim.End()








