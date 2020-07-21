import math
from math import *
import matplotlib
from matplotlib import pyplot as plt
x=[0,15,30,45,60,75,90,100,270,300,360]
y=[]

for i in x:
    #x.append(i)
    y.append(sin(radians(i)))

plt.plot(x,y,'-o')
plt.xlabel('degrees')
plt.ylabel('sin()')
plt.grid()
plt.show()





    
