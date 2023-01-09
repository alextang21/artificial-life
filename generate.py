import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
ratio = 1
for i in range(10):
	pyrosim.Send_Cube(name="Box", pos=[0,0,0.5+i] , size=[ratio,ratio,ratio])
	ratio *= 0.9
pyrosim.End()