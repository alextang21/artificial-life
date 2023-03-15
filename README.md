# Final Project

__Preface__

I ran my code overnight last night and it bugged out sometime over the night, I saw I had brain/body files in the 4000s, but I don't know when in the night it broke, so I tried it again today while I was eating dinner with my family for my mom's birthday. I was away for ~3 hours and when I came back it was still running but it was at 1800. Thus I calculated that it is able to do ~10 simulations every minute. This is 83 hours of constant running on my only laptop/computer available. Given the fact that I have other classes and commitments that require the use of my laptop, this was not feasible for me. I am now panic running 10 runs, 30 generations, 5 population size at 9:40pm in hopes that I can get 1500 simulations down for the submission. **Update** it failed again at ~10:30pm at 600 runs due to a pickling error that I had never seen before, but I looked it up and I believe(?) I have fixed it so I am running it again.

__Run__

By running "python3 search.py" will run a new set of simulations using the seeds that associate one run with one seed, and show the robot that has the furthest negative x-coordinate, and will draw out a plot of the fitnesses.

__Link Creation__

I created attributes of solution.py that created a random range of limbs, then used dictionaries and lists to determine other random characteristics of the robots like sensor/non-sensor and motor/non-motor, color, size, etc. These would be used to determine the joint position and the position of the links. The first link is initialized at a height that is determined by summing the sizes of each link and averaging them so that it wouldn't spawn inside the ground but also not spawning unreasonably high in the air. Then there is a for loop that goes through each link and puts them randomly on any of the six faces of the central body. It is not possible for my robot to have links created on the same face that the current link stemmed from, so while there is collision due to the small size and close proximity to each link, there is no collision that is avoidable while maintaining randomness in the placement and shape of the robot. Sensors neurons only control the link that is connected to and activates the motor attached to it.

The brain accessed the dictionaries made for the links in order to determine if there needed to be a sensor or motor neuron connected to the links, and if it was necessary, it would add a synapse connecting it to the other links.

__Mutation/Evolution__


<img width="300" alt="image" src="https://user-images.githubusercontent.com/67122357/222313751-e22d4831-43cc-4b0e-9a13-056849168604.png">

As shown above, the robot will mutate by changing the weights or creating/removing limbs. This will lead to some small robots, some larger robots, some robots that turn their limbs at harder or softer angles with ranging speeds, but all evolution/mutation works towards reaching a further x-coordinate from the origin.

__Methods__

To create a robot that does not have any distinct shape or any distinguishable or recreatable figure that performs a task such as moving in one direction is a difficult task to accomplish. The bulk of my code for this assignment was done in the "solution.py" file. This contained my SOLUTION class, which has many methods, one of which initializes attributes like the seed the randomness will follow, the number of limbs it will intialize with, information about the limbs, etc. It also contains the generation of the body and brain using Pyrosim, and uses that information to run a simulation using PyBullet. The vast majority of the simulations are done "directly" (without me being able to see them) and the fitness (how far it goes) is stored in txt files that are deleted after they are used so as to not take up unnecessary memory in my computer. Another method this class has is the "Mutate" method. This method uses a random number generator to decide if it should:

1. Change weights of the joints in order to alter the angle at which the joints move
2. Remove limbs and change weights of all remaining joints
3. Append limbs and change weights of all joints

This mutation function allows for a growing (or shrinking) robot that will be compared to the parent robot and, if the fitness is higher, replace the parent. If this robot is less successful, it will be discarded. This selection process is done in my "ParallelHillClimber.py" file, which contains the call to evolve and mutate children (who are initially direct copies of their parents). Once this evolution is complete, it will go through the Select funtion, which compares the parent's fitness to the child's fitness. This is done by gathering the parent's x-coordinate at the end of its simulation and doing the same with the children's, then comparing the two. If the child goes further, the child becomes the new parent and it is used for future evolutions for future generations.


__Diagram of Robot__

<img width="600" alt="image" src="https://user-images.githubusercontent.com/67122357/222313644-c4577be3-f5f8-4a98-9a67-706b38c218c1.png">


__Fitness plot__

<img width="640" alt="image" src="https://user-images.githubusercontent.com/67122357/222315165-55b7d574-9a4d-4ae0-ba6d-2e77dab5eb89.png">



__Credits__

Much inspiration drawn from Ludobots on Reddit, used Pyrosim, Pybullet, Numpy to create this project.
