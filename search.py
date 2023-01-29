import os

for i in range (5):

    print('iter=',i)
    os.system("python generate.py")
    os.system("python simulate.py")