import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
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
		os.system("rm fitness*.txt")
		self.parents = {}
		self.nextAvailableID = 0
		for i in range(c.populationSize):
			self.parents[i] = s.SOLUTION(self.nextAvailableID)
			self.nextAvailableID += 1


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
			if self.parents[i].fitness > self.children[i].fitness:
				self.parents[i] = self.children[i]

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		self.Print()
		self.Select()

	def Evaluate(self,solutions):
		for i in solutions:
			solutions[i].Start_Simulation("DIRECT")
		for i in solutions:
			solutions[i].Wait_For_Simulation_To_End()

	def Evolve(self):
		self.Evaluate(self.parents)
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()

	def Print(self):
		print("\n")
		for i in self.parents:
			print(self.parents[i].fitness, self.children[i].fitness)

	def Show_Best(self):
		bestFitness = float("inf")
		best = None
		for i in self.parents:
			if self.parents[i].fitness < bestFitness:
				best = self.parents[i]
				bestFitness = self.parents[i].fitness
		best.Start_Simulation("GUI")








