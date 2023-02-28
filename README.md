This Project was done for the ME495: Artificial Life course at Northwestern University 
The nature of this project was inspired by the Ludobots project found here: https://www.reddit.com/r/ludobots/ as well as the studies of Karl Sims a computer graphics artist and researcher, who is best known for using particle systems and artificial life in computer animation.

For assignment 8 we expand on the randomized 3D body of the previous assignment and design morphology and behavior for locomotion. To achieve this the code runs 5 different seeds through a specified number of generations, each with a specified number of populations. At each iteration the body and the brain change. The body is changed by adding or taking one of the body links, while the brain is altered by changing the weights of its synapses. The end goal is to evaluate which iteration provides a better fitness result (which in this case represents the ability to move to the left of the screen).

Once the program finishes running a plot is created with the 5 fitness curves, each for its respective seed, demonstrating the evolution (improvement in fitness) across generations. The following represents the evolution of 5 random seeds I generated with this code:

![image](https://user-images.githubusercontent.com/81761580/221753011-70fe3048-4129-4932-a804-2e46bd5199d0.png)

While the improvement isn't the most significant (which could be improved by increasing the number of populations and generations or by altering the mutate() function), we are able to see an upwards trend in all 5 fitness curves.

If you'd like to run this code simply run search.py

The below diagram visualizes the creation of the 3D Body and how the evolution happens from each seed. 

![image](https://user-images.githubusercontent.com/81761580/221759538-ab226e74-997b-442d-bccb-e434e7b00b3d.png)

![image](https://user-images.githubusercontent.com/81761580/221759588-8c46672e-12ba-42d7-9b51-61d5f3182d2c.png)

