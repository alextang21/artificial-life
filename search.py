import os
import parallelHillClimber
import solution as s
import constants as c
import matplotlib.pyplot as plt
import numpy

# for i in range(5):
# 	os.system("python3 generate.py")
# 	os.system("python3 simulate.py")
legend = []
fitnesses = {}
for i in range(2):
    phc = parallelHillClimber.PARALLEL_HILL_CLIMBER(i)
    phc.Evolve()
    phc.Show_Best()
    with open("fitnesses.npy", "rb") as file:
        data = numpy.load(file)
        fitnesses[i] = data[0][:-1]
    legend.append(f"Seed {i+1}")
for i in fitnesses:
    plt.plot(range(c.numberOfGenerations), fitnesses[i])
plt.xlabel('Generation Number')
plt.ylabel('Fitness')
plt.title('Fitness vs. Generation Number')
plt.legend(legend)
plt.show()