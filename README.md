# Final Project

__Preface__

I ran my code overnight last night and it bugged out sometime over the night, I saw I had brain/body files in the 4000s, but I don't know when in the night it broke, so I tried it again today while I was eating dinner with my family for my mom's birthday. I was away for ~3 hours and when I came back it was still running but it was at 1800. Thus I calculated that it is able to do ~10 simulations every minute. This is 83 hours of constant running on my only laptop/computer available. Given the fact that I have other classes and commitments that require the use of my laptop, this was not feasible for me. I am now panic running 10 runs, 30 generations, 5 population size at 9:40pm in hopes that I can get 1500 simulations down for the submission. **Update** it failed again at ~10:30pm at 600 runs due to a pickling error that I had never seen before, but I looked it up and I believe(?) I have fixed it so I am running it again. **SECOND UPDATE** it worked but I am running on a bit of a time crunch so I was not able to find and pickle as many robots as I wanted to for the video. I would prefer for this to be graded on the 44 point scale so that I can make up for the loss of points in previous assignments and because I believe I worked very hard on this with the time I was able to allot to this class during finals week.

__How to Run__

By running "python3 search.py" will run a new set of simulations using the seeds that associate one run with one seed, and show the robot that has the furthest negative x-coordinate, and will draw out a plot of the fitnesses.

__Video Explanation__

https://youtu.be/HBnu-FKAzuU


__GIF!__

![7ej54y](https://user-images.githubusercontent.com/67122357/225209556-2707933b-330d-4f0d-a4a5-1a5e6b855246.gif)


__Link Creation__


<img width="300" alt="image" src="https://user-images.githubusercontent.com/67122357/225208069-7f699bea-3b8c-4875-9dde-56482508dd9e.jpeg">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/67122357/225208277-cb55887c-8a7d-4769-8b75-87bd6e40eea7.jpeg">

I created attributes of solution.py that created a random range of limbs, then used dictionaries and lists to determine other random characteristics of the robots like sensor/non-sensor and motor/non-motor, color, size, etc. These would be used to determine the joint position and the position of the links. The first link is initialized at a height that is determined by summing the sizes of each link and averaging them so that it wouldn't spawn inside the ground but also not spawning unreasonably high in the air. Then there is a for loop that goes through each link and puts them randomly on any of the six faces of the central body. It is not possible for my robot to have links created on the same face that the current link stemmed from, so while there is collision due to the small size and close proximity to each link, there is no collision that is avoidable while maintaining randomness in the placement and shape of the robot. Sensors neurons only control the link that is connected to and activates the motor attached to it.

<img width="300" alt="image" src="https://user-images.githubusercontent.com/67122357/225208631-2b9eb647-e118-4ff0-95e2-7eb6ed53b98f.jpeg">


The brain accessed the dictionaries made for the links in order to determine if there needed to be a sensor or motor neuron connected to the links, and if it was necessary, it would add a synapse connecting it to the other links.

__Mutation/Evolution__

<img width="300" alt="image" src="https://user-images.githubusercontent.com/67122357/225208208-95c71613-3ec9-4058-b015-19e95943894d.jpeg">

As shown above, the robot will mutate by changing the weights or creating/removing limbs. This will lead to some small robots, some larger robots, some robots that turn their limbs at harder or softer angles with ranging speeds, but all evolution/mutation works towards reaching a further x-coordinate from the origin.

__Methods__

To create a robot that does not have any distinct shape or any distinguishable or recreatable figure that performs a task such as moving in one direction is a difficult task to accomplish. The bulk of my code for this assignment was done in the "solution.py" file. This contained my SOLUTION class, which has many methods, one of which initializes attributes like the seed the randomness will follow, the number of limbs it will intialize with, information about the limbs, etc. It also contains the generation of the body and brain using Pyrosim, and uses that information to run a simulation using PyBullet. The vast majority of the simulations are done "directly" (without me being able to see them) and the fitness (how far it goes) is stored in txt files that are deleted after they are used so as to not take up unnecessary memory in my computer. Another method this class has is the "Mutate" method. This method uses a random number generator to decide if it should:

1. Change weights of the joints in order to alter the angle at which the joints move
2. Remove limbs and change weights of all remaining joints
3. Append limbs and change weights of all joints

This mutation function allows for a growing (or shrinking) robot that will be compared to the parent robot and, if the fitness is higher, replace the parent. If this robot is less successful, it will be discarded. This selection process is done in my "ParallelHillClimber.py" file, which contains the call to evolve and mutate children (who are initially direct copies of their parents). Once this evolution is complete, it will go through the Select funtion, which compares the parent's fitness to the child's fitness. This is done by gathering the parent's x-coordinate at the end of its simulation and doing the same with the children's, then comparing the two. If the child goes further, the child becomes the new parent and it is used for future evolutions for future generations.


__Fitness plot__

<img width="640" alt="image" src="https://user-images.githubusercontent.com/67122357/225208028-b25a0df8-6ef5-47b8-9b6e-1a5f68ff7b57.png">

__Results__

A few notable robots showing improvement and evolution.

https://user-images.githubusercontent.com/67122357/225209265-531da76c-41bc-4329-8c84-f0648734f646.mov


https://user-images.githubusercontent.com/67122357/225209280-f44c053c-6d0d-4e3a-8be1-7feeaabc87f7.mov


https://user-images.githubusercontent.com/67122357/225209299-4fd6dcdb-8370-4390-a3aa-97bb5c7e88f6.mov


https://user-images.githubusercontent.com/67122357/225209324-f0d1db75-3b5c-4b38-9606-b4096d1e221f.mov


https://user-images.githubusercontent.com/67122357/225209346-e3beb424-b8df-4ec4-a227-d866f8980dbf.mov


https://user-images.githubusercontent.com/67122357/225209361-e0ccc936-fcc0-4db2-8fe3-ab5ddb559d4b.mov

My robots were, as made evident by the graph as well as the short clips shown above, able to make marked improvement as it evolved and changed both physical visible features like shape and size, as well as innate features like weights between synapses and sensors. I noticed that it would go from sitting there at the origin doing nothing to sometimes flipping itself around and over itself to roll or scoot across the negative x-axis. As shown by some of the seeds, the evolution would get stuck and plateau for the rest of the simulation. This could be accounted for by the lack of areas to grow, a poor initial shape, and the small amount of simulations I was ultimately able to run. I think these robots lacked a bit more attention to shape and ability to grow in more complex and smarter ways. For example I think that if I were able to make the robot grow in one direction to create a tail and use that to further the flipping motion, it would've gotten a lot farther than the little ball of energy that it became. Although I saw some improvement in the fitness of these robots as the generations went on, I wish I had more time to figure out how to make it even more successful and maybe play with some new fitnesses/goals for the robot to achieve. I hope to have the time to come back to this project and create more iterations of this robot without the stress of the final deadline overwhelming me. A video will be released soon, I wanted to spend a good amount of time on it and just simply did not have the time to do it before midnight, I hope you understand.

__Credits__

Much inspiration drawn from Ludobots on Reddit, used Pyrosim, Pybullet, Numpy to create this project.
