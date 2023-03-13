# MyBots

This Project is done for the ME495: Artificial Life course at Northwestern University The project is inspired by the Ludobots project found here: https://www.reddit.com/r/ludobots/

In this assignment we create a randomized 3D body by incorporating a random number of rectangular bodies linked to one another in all directions. Some of the bodies have sensors attributed to them. If they do their color is green instead of cyan.

To run this code simply run search.py

The below diagram visualizes the creation of the 3D Body. A cube 0 of randomized dimensions becomes the main parent of the structure with an absolute position. A first round of members is randomly created (in terms of dimensions and the the number of members), whose links to cube_0 are absolute. From there on, any randomized members added to subsequent members have relative positions.
Currently the code is limited in the number of subsequent members, which I intend to improve upon.

![image](https://user-images.githubusercontent.com/81761580/220251325-237e489f-a295-456b-866f-5c37146742f9.png)
