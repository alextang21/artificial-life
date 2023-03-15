import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time
import os
import constants as c

class SOLUTION:
	def __init__(self, myID, seed):
		random.seed(seed)
		numpy.random.seed(seed)
		self.limbs = {}
		self.num_limbs = [i for i in range(random.randint(3,4)*2+1)]
		self.sensors = numpy.random.randint(2, size = len(self.num_limbs))
		self.motors = numpy.random.randint(2, size = len(self.num_limbs))
		self.colors = {0: ["Blue", [0,0,1.0,1.0]], 1: ["Green", [0,1.0,0,1.0]]}
		self.motors[0] = 0

		self.limbs[0] = [self.sensors[0], self.motors[0], [1,1,1], self.colors[self.sensors[0]][0], self.colors[self.sensors[0]][1]]
		for i in range(1, len(self.num_limbs)):
			self.limbs[i] = [self.sensors[i], self.motors[i], numpy.random.rand(3) * random.randint(1,2)/2, self.colors[self.sensors[i]][0], self.colors[self.sensors[i]][1]]
		
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
		time.sleep(1)
		os.system("rm fitness" + str(self.myID) + ".txt")

	def Evaluate(self, directOrGUI):
		self.Start_Simulation(directOrGUI)
		self.Wait_For_Simulation_To_End()

	def Mutate(self):

		limbChange = random.randint(0,2)
		if limbChange == 0:
			i = random.randint(1,len(self.num_limbs)-1)
			self.limbs[i] = [self.sensors[i], self.motors[i], numpy.random.rand(3) * random.randint(1,2)/3+0.2, self.colors[self.sensors[i]][0], self.colors[self.sensors[i]][1]]
			self.weights = self.weights * 2 - 1
		
		if limbChange == 1:
			if len(self.limbs) > 8:
				for i in range(len(self.limbs)-2, len(self.limbs)):
					self.limbs.pop(i)
					self.num_limbs.pop()
					self.sensors = numpy.delete(self.sensors,-1)
					self.motors = numpy.delete(self.motors,-1)
			self.weights = numpy.random.rand(numpy.count_nonzero(self.sensors == 1), numpy.count_nonzero(self.motors == 1))
			self.weights = self.weights * 2 - 1

		elif limbChange == 2:
			if len(self.limbs) < 40:
				for i in range(len(self.limbs), len(self.limbs)+2):
					self.sensors = numpy.append(self.sensors,random.randint(0,1))
					self.motors = numpy.append(self.motors,random.randint(0,1))
					self.limbs[i] = [self.sensors[i], self.motors[i], numpy.random.rand(3) * random.randint(1,2)/3 + 0.2, self.colors[self.sensors[i]][0], self.colors[self.sensors[i]][1]]
					self.num_limbs.append(i)
				self.weights = numpy.random.rand(numpy.count_nonzero(self.sensors == 1), numpy.count_nonzero(self.motors == 1))
				self.weights = self.weights * 2 - 1
			
		self.Generate_Body()
		self.Generate_Brain()
			

	def Set_ID(self, ID):
		self.myID = ID

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.End()

	def Generate_Body(self):

		start_z = 0.0
		for i in self.limbs:
			start_z += sum(self.limbs[i][2])/3

		start_z /= 2


		leg1 = numpy.random.randint(2, size = 3)
		leg2 = numpy.random.randint(2, size = 3)
		leg3 = numpy.random.randint(2, size = 3)
		leg4 = numpy.random.randint(2, size = 3)
		# leg1 = numpy.array([1,1,1])
		# leg2 = numpy.array([1,1,1])
		# leg3 = numpy.array([1,1,1])
		# leg4 = numpy.array([1,1,1])

		
		pyrosim.Start_URDF(f"body{self.myID}.urdf")
		pyrosim.Send_Cube(name=f"Segment0", pos=[0,0,start_z], size=self.limbs[0][2], color=self.limbs[0][3], colorRGBA=self.limbs[0][4])
		# pyrosim.Send_Joint(name=f"Segment0_Segment1", parent=f"Segment0", child=f"Segment1",  type="revolute", position=[-self.limbs[0][2][0]/2*leg1[0],self.limbs[0][2][1]/2*leg1[1],start_z-(self.limbs[0][2][2]/2)-(self.limbs[1][2][2]/2)*leg1[2]], jointAxis = f"{leg1[0]} {leg1[1]} {leg1[2]}")
		# pyrosim.Send_Joint(name=f"Segment0_Segment2", parent=f"Segment0", child=f"Segment2",  type="revolute", position=[-self.limbs[0][2][0]/2*leg2[0],-self.limbs[0][2][1]/2*leg2[1],start_z-(self.limbs[0][2][2]/2)-(self.limbs[2][2][2]/2)*leg2[2]], jointAxis = f"{leg2[0]} {leg2[1]} {leg2[2]}")
		# pyrosim.Send_Joint(name=f"Segment0_Segment3", parent=f"Segment0", child=f"Segment3",  type="revolute", position=[self.limbs[0][2][0]/2*leg3[0],-self.limbs[0][2][1]/2*leg3[1],start_z-(self.limbs[0][2][2]/2)-(self.limbs[3][2][2]/2)*leg3[2]], jointAxis = f"{leg3[0]} {leg3[1]} {leg3[2]}")
		# pyrosim.Send_Joint(name=f"Segment0_Segment4", parent=f"Segment0", child=f"Segment4",  type="revolute", position=[self.limbs[0][2][0]/2*leg4[0],self.limbs[0][2][1]/2*leg4[1],start_z-(self.limbs[0][2][2]/2)-(self.limbs[4][2][2]/2)*leg4[2]], jointAxis = f"{leg4[0]} {leg4[1]} {leg4[2]}")
		pos = {0: 0}
		for i in range(1,3):
			leg = numpy.random.randint(2, size = 3)
			positions = {0: [0,0,start_z-self.limbs[0][2][2]/2-(self.limbs[i][2][2]/2)],
							1: [0,0,start_z+self.limbs[0][2][2]/2+(self.limbs[i][2][2]/2)],
							2: [-self.limbs[0][2][0]/2-(self.limbs[i][2][0]/2),0,start_z],
							3: [self.limbs[0][2][0]/2+(self.limbs[i][2][0]/2),0,start_z],
							4: [0,-self.limbs[0][2][1]/2-(self.limbs[i][2][1]/2),start_z],
							5: [0,self.limbs[0][2][1]/2+(self.limbs[i][2][1]/2),start_z]}
			choices = list(range(0,6))
			choices.pop(pos[i-1])
			pos[i] = random.choice(choices)
			pyrosim.Send_Joint(name=f"Segment0_Segment{i}", parent=f"Segment0", child=f"Segment{i}",  type="revolute", position=positions[pos[i]], jointAxis = f"{leg[0]} {leg[1]} {leg[2]}")
			# pyrosim.Send_Joint(name=f"Segment0_Segment2", parent=f"Segment0", child=f"Segment2",  type="revolute", position=[-self.limbs[0][2][0]/2,-self.limbs[0][2][1]/2,start_z-(self.limbs[0][2][2]/2)-(self.limbs[2][2][2]/2)], jointAxis = f"{leg2[0]} {leg2[1]} {leg2[2]}")
			# pyrosim.Send_Joint(name=f"Segment0_Segment3", parent=f"Segment0", child=f"Segment3",  type="revolute", position=[self.limbs[0][2][0]/2,-self.limbs[0][2][1]/2,start_z-(self.limbs[0][2][2]/2)-(self.limbs[3][2][2]/2)], jointAxis = f"{leg3[0]} {leg3[1]} {leg3[2]}")
			# pyrosim.Send_Joint(name=f"Segment0_Segment4", parent=f"Segment0", child=f"Segment4",  type="revolute", position=[self.limbs[0][2][0]/2,self.limbs[0][2][1]/2,start_z-(self.limbs[0][2][2]/2)-(self.limbs[4][2][2]/2)], jointAxis = f"{leg4[0]} {leg4[1]} {leg4[2]}")
		pos = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
		for i in range(1,len(self.num_limbs)-2):
			positions = {0: [0,0,-self.limbs[i][2][2]/2-(self.limbs[i+2][2][2]/2)],
						1: [0,0,self.limbs[i][2][2]/2+(self.limbs[i+2][2][2]/2)],
						2: [-self.limbs[i][2][0]/2-(self.limbs[i+2][2][0]/2),0,0],
						3: [self.limbs[i][2][0]/2+(self.limbs[i+2][2][0]/2),0,0],
						4: [0,-self.limbs[i][2][1]/2-(self.limbs[i+2][2][1]/2),0],
						5: [0,self.limbs[i][2][1]/2+(self.limbs[i+2][2][1]/2),0]}
			choices = list(range(0,6))
			if i <= 2:
				if i % 2 == 0:
					pyrosim.Send_Cube(name=f"Segment{i}", pos=[0,0,0], size=self.limbs[i][2], color=self.limbs[i][3], colorRGBA=self.limbs[i][4])
					pyrosim.Send_Joint(name=f"Segment{i}_Segment{i+2}", parent=f"Segment{i}", child=f"Segment{i+2}",  type="revolute", position=positions[random.randint(2,5)], jointAxis = "0 1 0")
				else:
					pyrosim.Send_Cube(name=f"Segment{i}", pos=[0,0,0], size=self.limbs[i][2], color=self.limbs[i][3], colorRGBA=self.limbs[i][4])
					pyrosim.Send_Joint(name=f"Segment{i}_Segment{i+2}", parent=f"Segment{i}", child=f"Segment{i+2}",  type="revolute", position=positions[random.randint(2,5)], jointAxis = "0 1 0")
			else:
				choices.pop(pos[i-2])
				pos[i] = random.choice(choices)
				if i % 2 == 0:
					pyrosim.Send_Cube(name=f"Segment{i}", pos=[0,0,0], size=self.limbs[i][2], color=self.limbs[i][3], colorRGBA=self.limbs[i][4])
					pyrosim.Send_Joint(name=f"Segment{i}_Segment{i+2}", parent=f"Segment{i}", child=f"Segment{i+2}",  type="revolute", position=positions[pos[i]], jointAxis = "0 1 0")
				else:
					pyrosim.Send_Cube(name=f"Segment{i}", pos=[0,0,0], size=self.limbs[i][2], color=self.limbs[i][3], colorRGBA=self.limbs[i][4])
					pyrosim.Send_Joint(name=f"Segment{i}_Segment{i+2}", parent=f"Segment{i}", child=f"Segment{i+2}",  type="revolute", position=positions[pos[i]], jointAxis = "0 1 0")

		# pyrosim.Send_Cube(name=f"Segment{self.num_limbs[-4]}", pos=[0,0,0], size=self.limbs[self.num_limbs[-4]][2], color=self.limbs[self.num_limbs[-4]][3], colorRGBA=self.limbs[self.num_limbs[-4]][4])
		# pyrosim.Send_Cube(name=f"Segment{self.num_limbs[-3]}", pos=[0,0,0], size=self.limbs[self.num_limbs[-3]][2], color=self.limbs[self.num_limbs[-3]][3], colorRGBA=self.limbs[self.num_limbs[-3]][4])
		pyrosim.Send_Cube(name=f"Segment{self.num_limbs[-2]}", pos=[0,0,0], size=self.limbs[self.num_limbs[-2]][2], color=self.limbs[self.num_limbs[-2]][3], colorRGBA=self.limbs[self.num_limbs[-2]][4])
		pyrosim.Send_Cube(name=f"Segment{self.num_limbs[-1]}", pos=[0,0,0], size=self.limbs[self.num_limbs[-1]][2], color=self.limbs[self.num_limbs[-1]][3], colorRGBA=self.limbs[self.num_limbs[-1]][4])

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
				# elif i == 2:
				# 	pyrosim.Send_Motor_Neuron( name = neuron_counter, jointName = f"Segment{i-2}_Segment{i}")
				# 	neuron_counter += 1
				# elif i == 3:
				# 	pyrosim.Send_Motor_Neuron( name = neuron_counter, jointName = f"Segment{i-3}_Segment{i}")
				# 	neuron_counter += 1
				else:
					pyrosim.Send_Motor_Neuron( name = neuron_counter, jointName = f"Segment{i-2}_Segment{i}")
					neuron_counter += 1

		for currentRow in range(numpy.count_nonzero(self.sensors == 1)):
			for currentColumn in range(numpy.count_nonzero(self.motors == 1)):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + numpy.count_nonzero(self.sensors == 1) , weight = self.weights[currentRow][currentColumn] )

		pyrosim.End()








