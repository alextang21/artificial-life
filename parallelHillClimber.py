import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import matplotlib.pyplot as plt
import numpy
import random
import time
import copy
import os
import constants as c
import solution as s

class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		os.system("rm brain*.nndf")
		os.system("rm body*.urdf")
		os.system("rm fitness*.txt")
		self.parents = {}
		self.nextAvailableID = 0
		self.currentGeneration = 0
		parentID = 0
		for i in range(c.populationSize):
			self.parents[i] = s.SOLUTION(self.nextAvailableID, parentID)
			self.nextAvailableID += 1
			parentID += 1
		self.fitnessMatrix = numpy.zeros((c.numberOfGenerations+1,c.populationSize))
		self.best = numpy.zeros((c.numberOfGenerations+1, len(self.parents)))
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
				self.best[self.currentGeneration][i] = min(self.parents[i].fitness, self.children[i].fitness) * -1
			if self.parents[i].fitness > self.children[i].fitness:
				self.parents[i] = self.children[i]
			if self.parents[i].fitness < self.best[self.currentGeneration][i]*-1:
				self.best[self.currentGeneration][i] = self.parents[i].fitness * -1
			else:
				self.best[self.currentGeneration][i] = self.best[self.currentGeneration-1][i]

			self.fitnessMatrix[self.currentGeneration][i] = self.best[self.currentGeneration][i]


		

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
		legend = []
		for i in self.parents:
			if self.parents[i].fitness < bestFitness:
				best = self.parents[i]
				bestFitness = self.parents[i].fitness
			plt.plot(range(c.numberOfGenerations), self.fitnessMatrix[:][i])
			legend.append(f"Seed {i+1}")
		print(self.fitnessMatrix[:])
		best.Start_Simulation("GUI")
		plt.xlabel('Generation Number')
		plt.ylabel('Fitness')
		plt.title('Fitness vs. Generation Number')
		plt.legend(legend)
		plt.show()






