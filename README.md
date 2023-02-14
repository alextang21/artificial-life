# Assignment 6

__Run__

By running "python3 simulate.py GUI 2" you will run a simulation of my code that uses the fitness2.txt file and brain2.nndf and body2.urdf files.
Alternatively, "python3 search.py" will run a new set of simulations and show the snake that has the furthest negative x-coordinate.

__Link Creation__

I created attributes of solution.py that detailed the number of links, it was a random range from 5-13 in my case and I used for loops that
ran through the number of links and assigned motor neurons to each, and sensor neurons for every other link. Sensor links are blue and non-sensor
neurons are black.

__Credits__

Much inspiration drawn from Ludobots on Reddit, used Pyrosim, Pybullet, Numpy to create this project.
