import sys
from simulation import SIMULATION

print("made it here A6")
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
print("made it here A7")
simulation.run()
print("made it here A8")
simulation.Get_Fitness()
print("made it here A9")