from solution import SOLUTION
import constants as c
import copy
import os
import random
import numpy

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        os.system("del" + " " + "brain*.nndf")
        os.system("del" + " " + "fitnessx*.txt")
        os.system("del" + " " + "world*.sdf")
        os.system("del" + " " + "body*.urdf")
        self.nextAvailableID = 0
        #self.parent = SOLUTION(self.nextAvailableID)
        self.parents = {}
        self.best_creature = []

        for parent in range (c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        # self.fitnessArray = numpy.zeros((c.numberOfGenerations+1,c.populationSize))
        # self.maxArray = numpy.zeros(c.numberOfGenerations+1)
        
    
    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate_gen(self.children, currentGeneration)
        self.Print(currentGeneration)
        self.Select()
        #print(self.fitnessArray)
        # if currentGeneration == c.numberOfGenerations-1:
        #     self.maxArray = numpy.min(self.fitnessArray, axis=1)
        #     print(self.maxArray)

    def Show_Best(self):
        best_parent = self.parents[0]
        for parent in self.parents.values():
            if parent.fitnessx < best_parent.fitnessx:
                best_parent = parent
        print("highest fit:", best_parent.fitnessx)
        best_parent.Start_Simulation("GUI")
        best_parent.Wait_For_Simulation_To_End()
        # all_values = self.parents.items()
        # highest_fitness = min(all_values, key=lambda x: x[1].fitnessx)
        # best_parent = highest_fitness[1]
        # best_parent.Start_Simulation("GUI")
        
    def Print(self, currentGeneration):
        print("\n")
        for i in self.parents:
            print("parent:", self.parents[i].fitnessx, "child:", self.children[i].fitnessx)
            #self.fitnessArray[currentGeneration,i] = self.children[i].fitnessx
        print("\n")
         
        
    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        best = -1
        for i in self.parents:
            if self.parents[i].fitnessx < self.children[i].fitnessx:
                self.parents[i] = self.children[i]
            best = max(self.parents[i].fitnessx, best)
        self.best_creature.append(best)
        
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
    
    
    def Evaluate(self, solutions):
        
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
                # for i in range(c.populationSize):
        #     if i == 0: 
        #         solutions[i].Start_Simulation("GUI")
        #     else:
        #         solutions[i].Start_Simulation("DIRECT")
            #change between direct and gui to see all populations or just the final/best
        # for i in range(c.populationSize):
        #     solutions[i].Wait_For_Simulation_To_End()
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def Evaluate_gen(self, solutions, generation):
        
        for i in solutions:
            if generation == 0: 
                solutions[i].Start_Simulation("GUI")
            else:
                solutions[i].Start_Simulation("DIRECT")
            #change between direct and gui to see all populations or just the final/best
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
    