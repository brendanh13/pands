# Messing with Histograms

import numpy as np

import matplotlib.pyplot as plt

fruit = np.array(["Apples", "Orange", "Banana"])
numbers = np.array([23, 77, 200])

plt.pie(numbers, labels = fruit)

#np.random.seed(1)
#normData = np.random.normal(size=10)

#xpoints = np.array(range(1,101))
#ypoints = xpoints * xpoints

#plt.hist(normData, color = "yellow")

#plt.plot(xpoints, ypoints, label = "xsquared")
#plt.plot(xpoints, xpoints, label = "straight", color = "blue")
plt.legend()

#randomPoints = np.random.randint(1,1000,100) 


#plt.scatter(xpoints, randomPoints, label = "random", color = "green")
plt.show()