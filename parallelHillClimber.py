import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import matplotlib.pyplot as plt
import numpy
import random
import time
import copy
import os
import pickle
import constants as c
import solution as s

class PARALLEL_HILL_CLIMBER:
	def __init__(self,seed):
		self.seed = seed
		os.system("rm brain*.nndf")
		os.system("rm body*.urdf")
		# os.system("rm fitness*.txt")
		self.parents = {}
		self.nextAvailableID = 0
		self.currentGeneration = 0
		parentID = 0
		for i in range(c.populationSize):
			self.parents[i] = s.SOLUTION(self.nextAvailableID, seed)
			self.nextAvailableID += 1
			parentID += 1
		self.fitnessMatrix = numpy.zeros((c.populationSize,c.numberOfGenerations+1))
		self.best = numpy.zeros((c.populationSize,c.numberOfGenerations+1))
		# self.bestMatrix = numpy.zeros((c.numberOfGenerations, c.populationSize))



	def Spawn(self):
		self.children = {}
		for i in self.parents:
			self.children[i] = copy.deepcopy(self.parents[i])
			self.children[i].Set_ID(self.nextAvailableID)
			self.nextAvailableID += 1

	def Mutate(self):
		for i in self.children:
			self.children[i].Mutate()

	def Select(self):
		for i in self.parents:
			if self.currentGeneration == 0:
				self.best[i][self.currentGeneration] = min(self.parents[i].fitness, self.children[i].fitness) * -1
			if self.parents[i].fitness > self.children[i].fitness:
				self.parents[i] = self.children[i]
			if self.parents[i].fitness < self.best[i][self.currentGeneration-1]*-1:
				self.best[i][self.currentGeneration] = self.parents[i].fitness * -1
			else:
				self.best[i][self.currentGeneration] = self.best[i][self.currentGeneration-1]

			self.fitnessMatrix[i][self.currentGeneration] = self.best[i][self.currentGeneration]


		

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		# self.Print()
		self.Select()
		self.currentGeneration += 1

	def Evaluate(self,solutions):
		for i in solutions:
			solutions[i].Start_Simulation("DIRECT")
		for i in solutions:
			solutions[i].Wait_For_Simulation_To_End()

	def Evolve(self):
		self.Evaluate(self.parents)
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()
		self.Print()

	def Print(self):
		print("\n")
		for i in self.parents:
			print(self.parents[i].fitness, self.children[i].fitness)

	def Show_Best(self):
		bestFitness = float("inf")
		best = None
		# legend = []
		print(self.parents[0].fitness)
		for i in self.parents:
			if self.parents[i].fitness < bestFitness:
				best = self.parents[i]
				bestFitness = self.parents[i].fitness
			# print(max(self.fitnessMatrix[i]))
			# plt.plot(range(c.numberOfGenerations), numpy.linspace(0,max(self.fitnessMatrix[i]), c.numberOfGenerations))
			# plt.plot(range(c.numberOfGenerations), self.fitnessMatrix[i][:-1])
			# legend.append(f"Seed {i+1}")
		
		with open("fitnesses.npy", "wb") as file:
			numpy.save("fitnesses.npy", self.fitnessMatrix[:])
		
		best.Start_Simulation("GUI")
		with open(f"best{self.seed}.bin", "wb") as f:
			pickle.dump(best, f)
		# plt.xlabel('Generation Number')
		# plt.ylabel('Fitness')
		# plt.title('Fitness vs. Generation Number')
		# plt.legend(legend)
		# plt.show()






