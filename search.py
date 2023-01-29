import os
import hillclimber
import solution as s

# for i in range(5):
# 	os.system("python3 generate.py")
# 	os.system("python3 simulate.py")

hc = hillclimber.HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()