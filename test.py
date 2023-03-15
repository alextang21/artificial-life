import os
import parallelHillClimber
import solution as s
import constants as c
import matplotlib.pyplot as plt
import numpy
import pickle

with open(f"best9.bin", "rb") as f:
    best = pickle.load(f)
    best.Start_Simulation("GUI")