from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        os.system("del" + " " +"brain*.nndf")
        os.system("del" + " " + "fitness*.txt")
        self.nextAvailableID = 0
        #self.parent = SOLUTION(self.nextAvailableID)
        self.parents = {}

        for parent in range (c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Show_Best(self):
        all_values = self.parents.items()
        lowest_fitness = min(all_values, key=lambda x: x[1].fitness)
        best_parent = lowest_fitness[1]
        best_parent.Start_Simulation("GUI")

    def Print(self):
        print("\n")
        for i in self.parents:
            print("parent:", self.parents[i].fitness, "child:", self.children[i].fitness)
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
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
        
    def Evolve(self):
        self.Evaluate(self.parents)
        
        # self.parent.Evaluate("GUI")
        # #self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()