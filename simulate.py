import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import time

backAmplitude = numpy.pi/3
backFrequency = 10
backPhaseOffset = 0
frontAmplitude = numpy.pi/2
frontFrequency = 10
frontPhaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
backTargetAngles = backAmplitude * numpy.sin(backFrequency * (numpy.linspace(0, 2*numpy.pi, 1000)) + backPhaseOffset)*(numpy.pi/6)
frontTargetAngles = frontAmplitude * numpy.sin(frontFrequency * (numpy.linspace(0, 2*numpy.pi, 1000)) + frontPhaseOffset)*(numpy.pi/6)
# numpy.save("data/backTargetAnglesData", backTargetAngles)
# numpy.save("data/frontTargetAnglesData", frontTargetAngles)
# exit()
for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(

		bodyIndex = robotId,

		jointName = b'Torso_BackLeg',

		controlMode = p.POSITION_CONTROL,

		targetPosition = backTargetAngles[i],

		maxForce = 200)
	pyrosim.Set_Motor_For_Joint(

		bodyIndex = robotId,

		jointName = b'Torso_FrontLeg',

		controlMode = p.POSITION_CONTROL,

		targetPosition = frontTargetAngles[i],

		maxForce = 200)
	time.sleep(1/600)
numpy.save("data/backLegSensorData", backLegSensorValues)
numpy.save("data/frontLegSensorData", frontLegSensorValues)
p.disconnect()

