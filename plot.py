import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt


data = genfromtxt('data.csv', delimiter=',')
x = data[:,0]
y = data[:,1]


plt.plot(x,y)
plt.ylabel('Speed')
plt.show()