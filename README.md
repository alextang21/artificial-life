# Assignment 8

__Run__

By running "python3 search.py" will run a new set of simulations and show the robot that has the furthest negative x-coordinate, and will draw out a plot of the fitnesses.

__Link Creation__

I created attributes of solution.py that detailed the number of links (random range of odd numbers from 9-21), then used dictionaries and lists to determine other random characteristics of the robots like sensor/non-sensor and motor/non-motor, color, size, etc. These would be used to determine the joint position and the position of the links. The first link is initialized at a height that is determined by summing the Z-coordinates of each link so that it wouldn't spawn inside the ground. Then there is a for loop that goes through each link and puts them on the four sides of the robot. Sensors neurons only control the link that is connected to and activates the motor attached to it.

The brain accessed the dictionaries made for the links in order to determine if there needed to be a sensor or motor neuron connected to the links.

__Mutation/Evolution__


<img width="300" alt="image" src="https://user-images.githubusercontent.com/67122357/222313751-e22d4831-43cc-4b0e-9a13-056849168604.png">

As shown above, the robot will mutate by changing the weights or creating/removing limbs.


__Diagram of Robot__

<img width="600" alt="image" src="https://user-images.githubusercontent.com/67122357/222313644-c4577be3-f5f8-4a98-9a67-706b38c218c1.png">


__Fitness plot__

<img width="640" alt="image" src="https://user-images.githubusercontent.com/67122357/222315165-55b7d574-9a4d-4ae0-ba6d-2e77dab5eb89.png">



__Credits__

Much inspiration drawn from Ludobots on Reddit, used Pyrosim, Pybullet, Numpy to create this project.
