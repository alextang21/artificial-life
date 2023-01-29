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

class HILL_CLIMBER:
	def __init__(self):
		self.parent = s.SOLUTION()

	def Spawn(self):
		self.child = copy.deepcopy(self.parent)

	def Mutate(self):
		self.child.Mutate()

	def Select(self):
		if self.parent.fitness > self.child.fitness:
			self.parent = self.child

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.child.Evaluate("DIRECT")
		self.Select()
		self.Print()

	def Evolve(self):
		self.parent.Evaluate("GUI")
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()

	def Print(self):
		print("\n")
		print(self.parent.fitness, self.child.fitness)

	def Show_Best(self):
		self.parent.Evaluate("GUI")