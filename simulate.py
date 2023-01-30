# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import time
# import constants as c
import sys

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
# backLegSensorValues = numpy.zeros(c.iterations)
# frontLegSensorValues = numpy.zeros(c.iterations)
# backTargetAngles = c.backAmplitude * numpy.sin(c.backFrequency * (numpy.linspace(0, 2*numpy.pi, c.iterations)) + c.backPhaseOffset)*(numpy.pi/6)
# frontTargetAngles = c.frontAmplitude * numpy.sin(c.frontFrequency * (numpy.linspace(0, 2*numpy.pi, c.iterations)) + c.frontPhaseOffset)*(numpy.pi/6)
# # numpy.save("data/backTargetAnglesData", backTargetAngles)
# # numpy.save("data/frontTargetAnglesData", frontTargetAngles)
# # exit()
# for i in range(c.iterations):
# 	p.stepSimulation()
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint(

# 		bodyIndex = robotId,

# 		jointName = b'Torso_BackLeg',

# 		controlMode = p.POSITION_CONTROL,

# 		targetPosition = backTargetAngles[i],

# 		maxForce = c.legForce)
# 	pyrosim.Set_Motor_For_Joint(

# 		bodyIndex = robotId,

# 		jointName = b'Torso_FrontLeg',

# 		controlMode = p.POSITION_CONTROL,

# 		targetPosition = frontTargetAngles[i],

# 		maxForce = c.legForce)
# 	time.sleep(1/600)
# numpy.save("data/backLegSensorData", backLegSensorValues)
# numpy.save("data/frontLegSensorData", frontLegSensorValues)
# p.disconnect()

from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()