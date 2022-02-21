# This program generates 10 random numbers, 
# prints them out and then prints out the top 3

# lists are used to store and manipulate the numbers

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

randomList = []

for i in range(0,10):
    n = random.randint(rangeFrom,rangeTo)
    randomList.append(n)
#print(randomlist)
print("{} random numbers\t {}".format(howMany,randomList))


topOnes = randomList.copy()
topOnes.sort(reverse = True)
print("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))