# Assignment 7

__Run__

By running "python3 search.py" will run a new set of simulations and show the snake that has the furthest negative x-coordinate.

__Link Creation__

I created attributes of solution.py that detailed the number of links (random range of odd numbers from 5-11), then used dictionaries and lists to determine other random characteristics of the robots like sensor/non-sensor and motor/non-motor, color, size, etc. These would be used to determine the joint position and the position of the links. The first link is initialized at a height that is determined by summing the Z-coordinates of each link so that it wouldn't spawn inside the ground. Then there is a for loop that goes through each link and puts them on either side of the robot. These joints are randomized so that they can either be parallel with the preceeding link or they can be at a 45 degree angle with the preceeding one, thus creating a 3-D occupying robot similar to some that I saw in Karm Sims' video. The links occasionally overlap due to the joint axes going in both the Y- and Z-axes, but this is unavoidable given the shapes and the fact that they need to be contiguous.

The brain accessed the dictionaries made for the links in order to determine if there needed to be a sensor or motor neuron connected to the links.

__Diagram__

![image](https://user-images.githubusercontent.com/67122357/220254001-0ace7dfc-06c2-4a6c-8b0f-ba86269ff8ae.png)


__Credits__

Much inspiration drawn from Ludobots on Reddit, used Pyrosim, Pybullet, Numpy to create this project.
