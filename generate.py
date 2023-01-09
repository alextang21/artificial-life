import pyrosim.pyrosim as pyrosim

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[2,-3,0.5] , size=[1,1,1])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Link_0", pos=[0,0,0.5] , size=[1,1,1])
	pyrosim.Send_Joint(name="Link0_Link1", parent="Link_0", child="Link_1", type="revolute", position=[0.5,0,1])
	pyrosim.Send_Cube(name="Link_1", pos=[0.5,0,0.5] , size=[1,1,1])
	pyrosim.Send_Joint(name="Link1_Link_2", parent="Link_1", child="Link_2", type="revolute", position=[1,0,0])
	pyrosim.Send_Cube(name="Link_2", pos=[0.5,0,-0.5] , size=[1,1,1])

	pyrosim.End()

Create_World()
Create_Robot()