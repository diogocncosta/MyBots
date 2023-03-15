# MyBots

## Acknowledgements
This project was created for the ME495: Artificial Life course at Northwestern University.

Sources and additional resources used in this video and project:
 - Ludobots project found here: https://www.reddit.com/r/ludobots/
 - Intro to Evolutionary Computation Alan Zucconi: https://www.alanzucconi.com/2016/04/0...
 - Research on "Flexible Muscle-Based Locomotion for Bipedal Creatures" by Thomas Geijtenbeek, Michiel van de Panne, Frank van der Stappen: https://www.goatstream.com/research/p...
 - The work of Karl Sims

## Welcome to Artificial Life!

Natural life has evolved on Earth for billions of years, but what if life existed in different contexts with different sources or motivations? Artificial life explores these possibilities by applying evolutionary principles to new situations. Let’s learn about it!

Disclaimer: If you just want a quick intro into the field of Artificial life, click the image below and check my 2min summary video of the topic. If you want to learn more and particularly abou my project, keep reading this blog post :)

[![Watch the video](https://img.youtube.com/vi/mKsERyVjuWg/maxresdefault.jpg)](https://youtu.be/mKsERyVjuWg)

## Evolutionary Programming and Artificial Evolution

You've probably heard of Darwin's "survival of the fittest" concept, which explains that the creatures that are best suited to their environment have a higher chance of survival and reproduction, while those that aren't are likely to die off. 

This same principle can be applied to computer programs - by randomly altering an approximate solution to a problem and testing its performance, we can continually improve it until we arrive at the best possible solution.

We are talking about evolutionary programming and it can be simplified into five iterative main steps: 

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/81761580/225052152-59941071-fa01-4b61-9d87-fa227c97b004.png" alt="5 steps" />
</p>


**Initialization**: Comes when we choose a starting point for the evolution, which can be randomized or specified.

**Duplication**: Producing multiple copies of the current solution to create a population.

**Mutation**: Randomly altering each copy in the population, with the extent and type of mutation being determined by the programmer.

**Evaluation**: Comparing the fitness of each individual in the population against a predetermined goal or environment.

**Selection**: Deciding which individuals are the most fit and allowing only those to move on to the next generation.

**Output**: The most fit individuals become the output and are used as the starting point for a new generation, with the process continuing iteratively until a desired result is achieved.

The number of generations is up to the programmer to determine, with the general rule being that more generations increase the chances of evolving a creature that excels at the task.

## This Project
You might be wondering "How can I actually implement these steps into something tangible?". Well I got you covered, for this project is - you guessed it - all about Artificial Life!

<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/81761580/225053195-eb1bc459-2724-4425-8932-2726c80c9363.gif" alt="GIF" />
</p>


### Initialization: 
When it came to generating a starting point, my goal was to create a randomized creature (which I will be refering to as a 'bot') made of randomized blocks. 
My algorithm starts by always creating a block of randomized dimensions that I designate as the torso of my bot. Afterwards I randomly assigning it a number of members (from 0 to 7). Each of these links is given random dimensions and a joint that connects it to one of the faces of the torso or another link, already attatched to the torso. Like the diagram below.

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/81761580/225172557-8acdded5-3669-4015-8abb-eea91b525d53.png" alt="GIF" />
 </p>

You may have also noticed that some of the links are green while others are blue. This is because our bodies have a brain that works as a closed loop system composed of sensors, synapses, motors and joints. Sensors collect information about the robot (e.g. the x position of the torso in space) that is then passed onto the motors by the synapses, which then send a torque to the links and change their position. The sensors are then fed new information and the loop repeats itself. This to say, the green links are the ones that have motors, while the blue ones are the ones without it (this too is randomly atributed).

### Duplication: 
Withing the code we stipulate the size of our population, that refers to the number of bots we will be working with at each generation.
To make a copy of a parent notheless, this happens within the parallelHillClimber.py file. We use the function Spawn() we created to make a deep copy of a parent and set as its child.

### Mutation: 
To ensure evolution we need to mutate the children of our parent bots. This refers to the function Mutate() in parallelHillClimber.py file. The function does two things:
 -  Randomly assigns the weights of the synapse connections
 -  If a bot has more than 5 links, it takes one away, if it has less it gives it one additional randomized one

### Evaluation: 
Where it comes to evaluation we used Evaluate() within the parellelHillClimber.py. Here, we run the simulation of both parents and children and used the fitness function to collect the information we need to then select the best bot. In this case we save the x position of the torso, so to measure how far to the left it is. The higher the better.

### Selection and Output: 
Selection happens within the function Select(), also within the parallelHillClimber.py file. This function compares each parent to its child using the outcome of their respective fitness functions. So the one with a higher fitness value (hence being able to walk furthest to the left) is kept and fed into the next generation of the code.

## Keeping it Real
Now, let’s be honest. Evolutionary coding isn’t necessarily the easiest thing. Even after 50,000 iterations, creatures created with the goal of walking furthest to the left barely moved from their original position, as you can see in the graph below:

<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/81761580/225106937-e9b52db6-ebae-492b-9b7d-411d6b1cbd50.jpg" alt="graph" />
</p>
                                                                                                                                         
But don’t let yourself be discouraged, for there are several resources available to help you along your journey in Artificial Life, like the ones on the top of this post. So go ahead, give it your best shot, learn from those resources or even build upon my code. I look forward see what you come up with! 

## How to run the project
To run this project I recommend downloading the files into a folder and opening it in vscode.
Once there, run the file "search.py" and you should see some magic happening!
                                    
Right now the code is set to have 1 seed, 1 member in the population and run for 1 generation. If you'd like to change this please follow the steps:
 - On line 5 of search.py change the range to the number of seeds you'd like to see
 - On constants.py change populationSize to the number you wish to have
 - On constants.py change numberOfGenerations to the number you wish to have

 Note that the code only shows the simulation for the first generation of bots and then the best one. The first simulations will instantly appear as you start running the code, while the final simulation will only appear when you hit enter, after the code has finish running.
