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

We are talking about evolutionary programming and it can be broken down into five main steps: 

<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/81761580/225052152-59941071-fa01-4b61-9d87-fa227c97b004.png" alt="5 steps" />
</p>


**Initialisation**: Comes when we choose a starting point for the evolution, which can be randomized or specified.

**Duplication**: Producing multiple copies of the current solution to create a population.

**Mutation**: Randomly altering each copy in the population, with the extent and type of mutation being determined by the programmer.

**Evaluation**: Comparing the fitness of each individual in the population against a predetermined goal or environment.

**Selection**: Deciding which individuals are the most fit and allowing only those to move on to the next generation.

**Output**: The most fit individuals become the output and are used as the starting point for a new generation, with the process continuing iteratively until a desired result is achieved.

The number of generations is up to the programmer to determine, with the general rule being that more generations increase the chances of evolving a creature that excels at the task.

## This Project
<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/81761580/225053195-eb1bc459-2724-4425-8932-2726c80c9363.gif" alt="GIF" />
</p>
## Keeping it Real
Now, let’s be honest. Evolutionary coding isn’t necessarily the easiest thing. I’ve tried my own version of it, and even after 50,000 iterations, creatures created with the goal of walking furthest to the left barely moved from their original position. But don’t let yourself be discouraged, for there are several resources available to help you along your journey in Artificial Life. I am attaching a few on the description of the video and I cannot wait to see what you come up with! 

