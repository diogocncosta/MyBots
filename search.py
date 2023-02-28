import os
from parallelHillClimber import PARALLEL_HILLCLIMBER
import matplotlib.pyplot as plt
import constants as c
for x in range (1,2):
    print("Random Seed {}".format(x))
    phc = PARALLEL_HILLCLIMBER()
    phc.Evolve()
    phc.Show_Best()

    plt.plot([i + 1 for i in range(c.numberOfGenerations)], 
            phc.best_creature, 
            label="random seed {}".format(x))

plt.title("Fitness of the best creature at each generation")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid()
plt.savefig("Best_fitnesses.jpg")