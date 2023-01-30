import os
import parallelHillClimber
import solution as s

# for i in range(5):
# 	os.system("python3 generate.py")
# 	os.system("python3 simulate.py")

phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()