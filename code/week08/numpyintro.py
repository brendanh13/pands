# NumPy
# Author: Brendan Heeney

import numpy as np

listOfNumbers = ([4,3,2,1])
numbers = np.array([1,2,4,5])


#listOfNumbers = listOfNumbers + 3
numbers = numbers * np.array([1,4,5,6])

print(listOfNumbers)
print(numbers)

randonNumbers = np.random.randint(100, 200, 5)
print(randonNumbers)